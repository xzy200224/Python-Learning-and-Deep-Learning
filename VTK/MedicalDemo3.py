import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_VERSION_NUMBER,
    vtkLookupTable,
    vtkVersion
)
from vtkmodules.vtkFiltersCore import (
    vtkFlyingEdges3D,
    vtkMarchingCubes,
    vtkStripper
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkImageMapToColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkImageActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    # 检查版本
    use_flying_edges = vtk_version_ok(8, 2, 0)
    # 获取路径
    file_name = get_program_parameters()

    # 创建一个颜色对象，以便我们可以更改颜色。使用RGB颜色空间。
    colors = vtkNamedColors()
    # 通过字符串引用RGB颜色
    colors.SetColor('SkinColor', [240, 184, 160, 255])
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    # 创建渲染器，渲染窗口和交互器。渲染器绘制到渲染窗口，交互器使得可以通过鼠标和键盘与渲染窗口中的数据进行交互。
    a_renderer = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(a_renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # 为渲染器设置背景颜色，并设置渲染窗口的大小（以像素为单位）。
    a_renderer.SetBackground(colors.GetColor3d('BkgColor'))
    ren_win.SetSize(640, 480)

    # vtkMetaImageReader类用于读取MetaImage文件，这是一种在医学成像数据中常用的格式。
    # 设置读取路径
    reader = vtkMetaImageReader()
    reader.SetFileName(file_name)
    # reader.Update(): 这行代码告诉读取器实际读取文件。这是必要的。
    # 因为VTK使用了一种管道架构，在这种架构中，操作不会实际执行，直到必要时，所以你需要调用Update()来告诉VTK实际执行读取操作。
    reader.Update()

    # 等值面或轮廓值500已知对应于患者的皮肤。三角形剥离器用于从等值面创建三角形带，这些带在许多系统上渲染得更快。
    if use_flying_edges:
        # vtkFlyingEdges3D和vtkMarchingCubes都是VTK库中用于提取等值面的类。
        try:
            skin_extractor = vtkFlyingEdges3D()
        except AttributeError:
            skin_extractor = vtkMarchingCubes()
    else:
        skin_extractor = vtkMarchingCubes()

    # 皮肤提取器将提取出数据中值为500的等值面。
    skin_extractor.SetInputConnection(reader.GetOutputPort())
    skin_extractor.SetValue(0, 500)
    skin_extractor.Update()
    # vtkStripper主要用于优化几何图形的渲染，通过将连续的三角形转换为三角形条带，可以减少渲染时所需的顶点数量，从而提高渲染效率。
    skin_stripper = vtkStripper()
    skin_stripper.SetInputConnection(skin_extractor.GetOutputPort())
    skin_stripper.Update()
    # 设置映射器
    skin_mapper = vtkPolyDataMapper()
    skin_mapper.SetInputConnection(skin_stripper.GetOutputPort())
    skin_mapper.ScalarVisibilityOff()
    # 设置演员
    skin = vtkActor()
    skin.SetMapper(skin_mapper)
    skin.GetProperty().SetDiffuseColor(colors.GetColor3d('SkinColor'))
    skin.GetProperty().SetSpecular(0.3)
    skin.GetProperty().SetSpecularPower(20)

    # 等值面或轮廓值1150已知对应于患者的骨骼。三角形剥离器用于从等值面创建三角形带，这些带在许多系统上渲染得更快。
    if use_flying_edges:
        try:
            bone_extractor = vtkFlyingEdges3D()
        except AttributeError:
            bone_extractor = vtkMarchingCubes()
    else:
        bone_extractor = vtkMarchingCubes()
    # 骨骼提取器将提取出数据中值为1150的等值面。
    bone_extractor.SetInputConnection(reader.GetOutputPort())
    bone_extractor.SetValue(0, 1150)
    # vtkStripper主要用于优化几何图形的渲染，通过将连续的三角形转换为三角形条带，可以减少渲染时所需的顶点数量，从而提高渲染效率。
    bone_stripper = vtkStripper()
    bone_stripper.SetInputConnection(bone_extractor.GetOutputPort())
    # 设置映射器
    bone_mapper = vtkPolyDataMapper()
    bone_mapper.SetInputConnection(bone_stripper.GetOutputPort())
    bone_mapper.ScalarVisibilityOff()
    # 设置演员
    bone = vtkActor()
    bone.SetMapper(bone_mapper)
    bone.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))

    # vtkOutlineFilter()被用来创建一个轮廓过滤器，这个过滤器可以生成头部CT数据集的边界框。
    outline_data = vtkOutlineFilter()
    outline_data.SetInputConnection(reader.GetOutputPort())
    outline_data.Update()
    map_outline = vtkPolyDataMapper()
    map_outline.SetInputConnection(outline_data.GetOutputPort())
    outline = vtkActor()
    outline.SetMapper(map_outline)
    outline.GetProperty().SetColor(colors.GetColor3d('Black'))

    # 现在我们正在创建通过体积的三个正交平面。每个平面使用不同的纹理映射，因此具有不同的颜色。
    # 首先创建一个黑/白查找表。
    bw_lut = vtkLookupTable()
    # 设置了颜色表的范围
    bw_lut.SetTableRange(0, 2000)
    # 设置了饱和度范围，这里是0到0，表示完全去除饱和度。
    bw_lut.SetSaturationRange(0, 0)
    # 设置了色调范围，这里是0到0，表示完全去除色调。
    bw_lut.SetHueRange(0, 0)
    # 设置了值范围，这里是0到1，表示完全饱和。
    bw_lut.SetValueRange(0, 1)
    # 构建颜色表
    bw_lut.Build()

    # 现在创建一个查找表，该表包含完整的色调圆圈（来自HSV）。
    hue_lut = vtkLookupTable()
    hue_lut.SetTableRange(0, 2000)
    hue_lut.SetHueRange(0, 1)
    hue_lut.SetSaturationRange(1, 1)
    hue_lut.SetValueRange(1, 1)
    hue_lut.Build()
    # 最后，创建一个查找表，该表具有单一的色调，但在色调的饱和度范围内。
    sat_lut = vtkLookupTable()
    sat_lut.SetTableRange(0, 2000)
    sat_lut.SetHueRange(0.6, 0.6)
    sat_lut.SetSaturationRange(0, 1)
    sat_lut.SetValueRange(1, 1)
    sat_lut.Build()  # effective built

    # 创建三个平面中的第一个。过滤器vtkImageMapToColors通过上面创建的相应查找表映射数据。
    # vtkImageActor是vtkProp的一种类型，可以方便地在单个四边形平面上显示图像。
    # 它使用纹理映射，因此速度相当快。（注意：输入图像必须是无符号字符值，这是vtkImageMapToColors生成的。）
    # 还要注意，通过指定DisplayExtent，管道请求此范围的数据，vtkImageMapToColors只处理一片数据。
    sagittal_colors = vtkImageMapToColors()
    # 设置输入连接，这里的输入是 reader 的输出。
    sagittal_colors.SetInputConnection(reader.GetOutputPort())
    # 设置查找表
    sagittal_colors.SetLookupTable(bw_lut)
    sagittal_colors.Update()
    # 创建actor和设置mapper
    sagittal = vtkImageActor()
    sagittal.GetMapper().SetInputConnection(sagittal_colors.GetOutputPort())
    # 设置图像actor的显示范围。这里的范围是一个六元组，表示在 x、y 和 z 方向上的最小和最大索引。
    sagittal.SetDisplayExtent(128, 128, 0, 255, 0, 255)
    # 强制图像演员为不透明。
    sagittal.ForceOpaqueOn()

    # 创建三个平面中的第二个（轴向平面）。我们使用与之前相同的方法，只是范围不同。
    axial_colors = vtkImageMapToColors()
    axial_colors.SetInputConnection(reader.GetOutputPort())
    axial_colors.SetLookupTable(hue_lut)
    axial_colors.Update()
    axial = vtkImageActor()
    axial.GetMapper().SetInputConnection(axial_colors.GetOutputPort())
    axial.SetDisplayExtent(0, 255, 0, 255, 128, 128)
    axial.ForceOpaqueOn()

    #  创建三个平面中的第三个（冠状平面）。我们使用与之前相同的方法，只是范围不同。
    coronal_colors = vtkImageMapToColors()
    coronal_colors.SetInputConnection(reader.GetOutputPort())
    coronal_colors.SetLookupTable(sat_lut)
    coronal_colors.Update()
    coronal = vtkImageActor()
    coronal.GetMapper().SetInputConnection(coronal_colors.GetOutputPort())
    coronal.SetDisplayExtent(0, 255, 128, 128, 0, 255)
    coronal.ForceOpaqueOn()

    # 创建数据的初始视图。FocalPoint和Position形成一个向量方向。
    # 稍后（ResetCamera()方法）将使用此向量来定位相机，使其朝着这个方向查看数据。
    a_camera = vtkCamera()
    a_camera.SetViewUp(0, 0, -1)
    a_camera.SetPosition(0, -1, 0)
    a_camera.SetFocalPoint(0, 0, 0)
    a_camera.ComputeViewPlaneNormal()
    a_camera.Azimuth(30.0)
    a_camera.Elevation(30.0)

    # 将演员添加到渲染器。
    a_renderer.AddActor(outline)
    a_renderer.AddActor(sagittal)
    a_renderer.AddActor(axial)
    a_renderer.AddActor(coronal)
    a_renderer.AddActor(skin)
    a_renderer.AddActor(bone)

    # 为此示例关闭骨头。
    bone.VisibilityOff()

    # 将皮肤设置为半透明。
    skin.GetProperty().SetOpacity(0.5)

    # 创建初始的相机视图。Dolly()方法将相机向FocalPoint移动，从而放大图像。
    a_renderer.SetActiveCamera(a_camera)

    # 直接在 vtkRenderer 上调用 Render() 是严格禁止的。
    # 只有在 vtkRenderWindow 上调用 Render() 是有效的调用。
    ren_win.SetWindowName('MedicalDemo3')
    ren_win.Render()

    a_renderer.ResetCamera()
    a_camera.Dolly(1.5)

    # 注意，当相机移动发生时（如在Dolly()方法中），剪裁平面通常需要调整。
    # 剪裁平面由两个平面组成：沿视图方向的近平面和远平面。近平面剪裁掉平面前的对象；远平面剪裁掉平面后的对象。
    # 这样，只有在平面之间绘制的内容才会实际渲染。
    a_renderer.ResetCameraClippingRange()

    # 与数据进行交互。
    ren_win.Render()
    iren.Initialize()
    iren.Start()


def get_program_parameters():
    # 用于处理命令行参数和选项。它可以生成帮助和使用消息，并在用户给出程序无法理解的参数时发出错误。
    import argparse
    # description,epilogue字符串将在命令行中显示帮助信息
    description = 'The skin and bone is extracted from a CT dataset of the head.'
    epilogue = '''
    Derived from VTK/Examples/Cxx/Medical3.cxx
    This example reads a volume dataset, extracts two isosurfaces that
     represent the skin and bone, creates three orthogonal planes
     (sagittal, axial, coronal), and displays them.
    '''
    # argparse.ArgumentParser 对象，该对象将用于解析命令行参数。
    # 在创建 ArgumentParser 对象时，函数将之前定义的描述和尾注作为参数传递给 ArgumentParser。
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    #  add_argument 方法来添加一个命令行参数。
    #  这个参数的名称是 'filename'，并且它的帮助信息是 'FullHead.mhd.'。
    parser.add_argument('filename', help='FullHead.mhd.')
    #  parse_args 方法来解析命令行参数。
    #  parse_args 方法返回一个命名空间，其中包含所有的命令行参数。
    args = parser.parse_args()
    # 函数返回 'filename' 参数的值
    return args.filename


def vtk_version_ok(major, minor, build):
    # 检查当前的VTK（Visualization Toolkit）版本是否满足给定的版本要求
    """
    Check the VTK version.

    :param major: Major version.
    :param minor: Minor version.
    :param build: Build version.
    :return: True if the requested VTK version is greater or equal to the actual VTK version.
    """
    needed_version = 10000000000 * int(major) + 100000000 * int(minor) + int(build)
    try:
        vtk_version_number = VTK_VERSION_NUMBER
    except AttributeError:  # as error:
        ver = vtkVersion()
        vtk_version_number = 10000000000 * ver.GetVTKMajorVersion() + 100000000 * ver.GetVTKMinorVersion() \
                             + ver.GetVTKBuildVersion()
    if vtk_version_number >= needed_version:
        return True
    else:
        return False


if __name__ == '__main__':
    main()