# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_VERSION_NUMBER,
    vtkVersion
)
from vtkmodules.vtkFiltersCore import (
    vtkFlyingEdges3D,
    vtkMarchingCubes,
    vtkStripper
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

"""
皮肤和骨骼等值面。
"""

def main():
    # 检查版本
    use_flying_edges = vtk_version_ok(8, 2, 0)
    # 获取路径
    file_name = get_program_parameters()

    # 创建一个颜色对象，以便我们可以更改颜色。使用RGB颜色空间。
    colors = vtkNamedColors()
    colors.SetColor('SkinColor', [240, 184, 160, 255])
    colors.SetColor('BackfaceColor', [255, 229, 200, 255])
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    # 创建渲染器，渲染窗口和交互器。渲染器
    # 在渲染窗口中绘图，交互器使得可以通过鼠标和
    # 键盘与渲染窗口中的数据进行交互。
    #
    a_renderer = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(a_renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # 读取头部的CT数据集。
    reader = vtkMetaImageReader()
    reader.SetFileName(file_name)

    # 等值面，或者说轮廓值为500，已知对应于病人的皮肤。
    # 三角形剥离器用于从等值面创建三角形带，
    if use_flying_edges:
        try:
            skin_extractor = vtkFlyingEdges3D()
        except AttributeError:
            skin_extractor = vtkMarchingCubes()
    else:
        skin_extractor = vtkMarchingCubes()
    # 皮肤提取器将提取出数据中值为500的等值面。
    skin_extractor.SetInputConnection(reader.GetOutputPort())
    skin_extractor.SetValue(0, 500)
    # vtkStripper主要用于优化几何图形的渲染，通过将连续的三角形转换为三角形条带，可以减少渲染时所需的顶点数量，从而提高渲染效率。
    skin_stripper = vtkStripper()
    skin_stripper.SetInputConnection(skin_extractor.GetOutputPort())
    # 设置映射器
    skin_mapper = vtkPolyDataMapper()
    skin_mapper.SetInputConnection(skin_stripper.GetOutputPort())

    # 关闭标量可见性，将不会使用标量数据来映射颜色，而是使用固定的颜色或者材质属性来渲染对象。
    skin_mapper.ScalarVisibilityOff()
    # 设置actor
    skin = vtkActor()
    skin.SetMapper(skin_mapper)
    skin.GetProperty().SetDiffuseColor(colors.GetColor3d('SkinColor'))
    skin.GetProperty().SetSpecular(0.3)
    skin.GetProperty().SetSpecularPower(20)
    skin.GetProperty().SetOpacity(0.5)
    # 设置了back_prop
    back_prop = vtkProperty()
    back_prop.SetDiffuseColor(colors.GetColor3d('BackfaceColor'))
    skin.SetBackfaceProperty(back_prop)

    # 等值面，或者说轮廓值为1150，已知对应于病人的骨骼。
    # 三角形剥离器用于从等值面创建三角形带，
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
    # 设置actor
    bone = vtkActor()
    bone.SetMapper(bone_mapper)
    bone.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))

    # vtkOutlineFilter()被用来创建一个轮廓过滤器，这个过滤器可以生成头部CT数据集的边界框。
    outline_data = vtkOutlineFilter()
    outline_data.SetInputConnection(reader.GetOutputPort())
    # 设置映射器
    map_outline = vtkPolyDataMapper()
    map_outline.SetInputConnection(outline_data.GetOutputPort())
    # 设置actor
    outline = vtkActor()
    outline.SetMapper(map_outline)
    outline.GetProperty().SetColor(colors.GetColor3d('Black'))

    # 设置相机。
    a_camera = vtkCamera()
    a_camera.SetViewUp(0, 0, -1)
    a_camera.SetPosition(0, -1, 0)
    a_camera.SetFocalPoint(0, 0, 0)
    a_camera.ComputeViewPlaneNormal()
    a_camera.Azimuth(30.0)
    a_camera.Elevation(30.0)

    # 将actor添加到渲染器。创建一个初始的相机视图。
    # Dolly()方法将相机向FocalPoint移动，
    # 从而放大图像。
    a_renderer.AddActor(outline)
    a_renderer.AddActor(skin)
    a_renderer.AddActor(bone)
    a_renderer.SetActiveCamera(a_camera)
    a_renderer.ResetCamera()
    a_camera.Dolly(1.5)

    # 设置渲染器的背景颜色，并设置渲染窗口的大小
    # （以像素为单位）。
    a_renderer.SetBackground(colors.GetColor3d('BkgColor'))
    ren_win.SetSize(640, 480)
    ren_win.SetWindowName('MedicalDemo2')

    # 注意，当相机移动发生（如在Dolly()
    # 方法中），剪裁平面通常需要调整。剪裁平面
    # 由两个平面组成：沿视图方向的近平面和远平面。近平面剪裁掉平面前的对象；远平面剪裁掉平面后的对象。
    # 这样，只有在平面之间绘制的内容才会实际渲染。
    a_renderer.ResetCameraClippingRange()

    # 初始化事件循环，然后开始它。
    iren.Initialize()
    iren.Start()


def get_program_parameters():
    import argparse
    description = '从头部的CT数据集中提取皮肤和骨骼。'
    epilogue = '''
    源自VTK/Examples/Cxx/Medical2.cxx
    这个例子读取一个体积数据集，提取代表皮肤和骨骼的两个等值面，
    然后显示它。
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    args = parser.parse_args()
    return args.filename


def vtk_version_ok(major, minor, build):
    """
    检查VTK版本。

    :param major: 主版本。
    :param minor: 次版本。
    :param build: 构建版本。
    :return: 如果请求的VTK版本大于或等于实际的VTK版本，则返回True。
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