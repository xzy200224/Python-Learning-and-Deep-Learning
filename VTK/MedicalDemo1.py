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
    vtkMarchingCubes
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
The skin extracted from a CT dataset of the head.
"""

def main():
    # 检查版本
    use_flying_edges = vtk_version_ok(8, 2, 0)
    # 获取路径
    file_name = get_program_parameters()
    # 创建一个颜色对象，以便我们可以更改颜色。使用RGB颜色空间。
    colors = vtkNamedColors()
    # 通过字符串引用RGB颜色
    colors.SetColor('SkinColor', [240, 184, 160, 255])
    colors.SetColor('BackfaceColor', [255, 229, 200, 255])
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    # 创建渲染器，渲染窗口和交互器。渲染器绘制到渲染窗口，交互器使得可以通过鼠标和键盘与渲染窗口中的数据进行交互。
    a_renderer = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(a_renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # vtkMetaImageReader类用于读取MetaImage文件，这是一种在医学成像数据中常用的格式。
    # 设置读取路径
    reader = vtkMetaImageReader()
    reader.SetFileName(file_name)

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
    # 创建皮肤的映射器
    skin_mapper = vtkPolyDataMapper()
    skin_mapper.SetInputConnection(skin_extractor.GetOutputPort())
    # 关闭了标量可见性。在VTK中，标量可见性决定了是否使用标量数据来颜色化对象。
    # 如果标量可见性被关闭，那么对象将被渲染为单一颜色。
    # 在这个例子中，关闭标量可见性意味着皮肤将被渲染为单一颜色，而不是根据标量数据变化颜色。
    skin_mapper.ScalarVisibilityOff()

    # 创建皮肤的actor，设置颜色和背面属性。
    skin = vtkActor()
    skin.SetMapper(skin_mapper)
    skin.GetProperty().SetDiffuseColor(colors.GetColor3d('SkinColor'))
    # 设置了back_prop的颜色
    back_prop = vtkProperty()
    back_prop.SetDiffuseColor(colors.GetColor3d('BackfaceColor'))
    # 将back_prop设置为皮肤对象的背面属性。在VTK中，每个对象都有前面和背面，这两个面可以有不同的属性。
    skin.SetBackfaceProperty(back_prop)

    # vtkOutlineFilter类用于生成数据集的轮廓。轮廓是一个包围数据集的框。
    outline_data = vtkOutlineFilter()
    outline_data.SetInputConnection(reader.GetOutputPort())
    # 创建轮廓的映射器
    map_outline = vtkPolyDataMapper()
    map_outline.SetInputConnection(outline_data.GetOutputPort())
    # 创建轮廓的actor，设置颜色
    outline = vtkActor()
    outline.SetMapper(map_outline)
    outline.GetProperty().SetColor(colors.GetColor3d('Black'))

    # 建了一个vtkCamera的实例，表示一个虚拟相机
    a_camera = vtkCamera()
    # 设置了相机的上方向，这意味着相机的上方向是向负Z轴
    a_camera.SetViewUp(0, 0, -1)
    # 置了相机的位置和焦点。相机的位置是(0, -1, 0)，焦点是(0, 0, 0)。
    a_camera.SetPosition(0, -1, 0)
    a_camera.SetFocalPoint(0, 0, 0)
    # 计算了相机的视平面法线。视平面法线是相机的方向。
    # 在VTK中，视平面的法线是一个向量，它垂直于视平面。这个方法会根据当前的位置和焦点自动计算法线。
    a_camera.ComputeViewPlaneNormal()
    # 将相机在水平方向上旋转30度。在VTK中，Azimuth方法用于绕着视平面的法线旋转相机。
    a_camera.Azimuth(30.0)
    # 将相机在垂直方向上旋转30度。在VTK中，Elevation方法用于绕着视平面的右方向旋转相机。
    a_camera.Elevation(30.0)

    # 将演员（actors）添加到渲染器（renderer），创建了一个初始的相机视图，并通过Dolly()方法移动相机以放大图像。
    a_renderer.AddActor(outline)
    a_renderer.AddActor(skin)
    a_renderer.SetActiveCamera(a_camera)
    a_renderer.ResetCamera()
    a_camera.Dolly(1.5)

    # 设置了渲染器的背景颜色，并设置了渲染窗口的大小和名称
    a_renderer.SetBackground(colors.GetColor3d('BkgColor'))
    ren_win.SetSize(640, 480)
    ren_win.SetWindowName('MedicalDemo1')

    # ResetCameraClippingRange()方法来调整剪裁平面。
    # 剪裁平面由两个平面组成：沿视图方向的近平面和远平面。近平面会剪裁掉平面前面的对象，远平面会剪裁掉平面后面的对象。
    # 这样，只有在两个平面之间的对象才会被渲染。
    a_renderer.ResetCameraClippingRange()

    # Initialize the event loop and then start it.
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