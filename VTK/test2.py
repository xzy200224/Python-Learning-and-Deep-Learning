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
from vtkmodules.vtkIOImage import vtkNIFTIImageReader
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
    # 获取路径
    file_name = 'T1.nii.gz'

    # 创建一个颜色对象，以便我们可以更改颜色。使用RGB颜色空间。
    colors = vtkNamedColors()
    # 通过字符串引用RGB颜色
    colors.SetColor('SkinColor', [240, 184, 160, 255])
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    # 创建渲染器，渲染窗口和交互器。渲染器绘制到渲染窗口，交互器使得可以通过鼠标和键盘与渲染窗口中的数据进行交互。
    #
    a_renderer = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(a_renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # 为渲染器设置背景颜色，并设置渲染窗口的大小（以像素为单位）。
    #
    a_renderer.SetBackground(colors.GetColor3d('BkgColor'))
    ren_win.SetSize(640, 480)

    # vtkMetaImageReader类用于读取MetaImage文件，这是一种在医学成像数据中常用的格式。
    # 设置读取路径
    reader = vtkNIFTIImageReader()
    reader.SetFileName(file_name)
    # reader.Update(): 这行代码告诉读取器实际读取文件。这是必要的。
    # 因为VTK使用了一种管道架构，在这种架构中，操作不会实际执行，直到必要时，所以你需要调用Update()来告诉VTK实际执行读取操作。
    reader.Update()

    # vtkFlyingEdges3D和vtkMarchingCubes都是VTK库中用于提取等值面的类。
    try:
        skin_extractor = vtkFlyingEdges3D()
    except AttributeError:
        skin_extractor = vtkMarchingCubes()

    # 皮肤提取器将提取出数据中值为500的等值面。
    skin_extractor.SetInputConnection(reader.GetOutputPort())
    skin_extractor.SetValue(0, 60)
    skin_extractor.Update()

    skin_stripper = vtkStripper()
    skin_stripper.SetInputConnection(skin_extractor.GetOutputPort())
    skin_stripper.Update()

    skin_mapper = vtkPolyDataMapper()
    skin_mapper.SetInputConnection(skin_stripper.GetOutputPort())
    skin_mapper.ScalarVisibilityOff()

    skin = vtkActor()
    skin.SetMapper(skin_mapper)
    skin.GetProperty().SetDiffuseColor(colors.GetColor3d('SkinColor'))
    skin.GetProperty().SetSpecular(0.3)
    skin.GetProperty().SetSpecularPower(20)


    try:
        bone_extractor = vtkFlyingEdges3D()
    except AttributeError:
        bone_extractor = vtkMarchingCubes()

    bone_extractor.SetInputConnection(reader.GetOutputPort())
    bone_extractor.SetValue(0, 100)

    bone_stripper = vtkStripper()
    bone_stripper.SetInputConnection(bone_extractor.GetOutputPort())

    bone_mapper = vtkPolyDataMapper()
    bone_mapper.SetInputConnection(bone_stripper.GetOutputPort())
    bone_mapper.ScalarVisibilityOff()

    bone = vtkActor()
    bone.SetMapper(bone_mapper)
    bone.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))

    # 外轮廓提供了数据的上下文。
    #
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
    bw_lut.SetTableRange(0, 2000)
    bw_lut.SetSaturationRange(0, 0)
    bw_lut.SetHueRange(0, 0)
    bw_lut.SetValueRange(0, 1)
    bw_lut.Build()  # effective built

    # 现在创建一个查找表，该表包含完整的色调圆圈（来自HSV）。
    hue_lut = vtkLookupTable()
    hue_lut.SetTableRange(0, 2000)
    hue_lut.SetHueRange(0, 1)
    hue_lut.SetSaturationRange(1, 1)
    hue_lut.SetValueRange(1, 1)
    hue_lut.Build()  # effective built

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
    sagittal_colors.SetInputConnection(reader.GetOutputPort())
    sagittal_colors.SetLookupTable(bw_lut)
    sagittal_colors.Update()

    sagittal = vtkImageActor()
    sagittal.GetMapper().SetInputConnection(sagittal_colors.GetOutputPort())
    sagittal.SetDisplayExtent(128, 128, 0, 255, 0, 255)
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

if __name__ == '__main__':
    # 调用函数
    main()
    # Read the .nii.gz file
    # image = sitk.ReadImage('T1.nii.gz')
    # numpy_array = sitk.GetArrayFromImage(image)
    # print(np.min(numpy_array), np.max(numpy_array))