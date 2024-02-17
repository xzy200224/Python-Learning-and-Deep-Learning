import numpy as np
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
from vtkmodules.vtkIOImage import vtkNIFTIImageReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkProperty,
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
    reader = vtkNIFTIImageReader()
    reader.SetFileName(file_name)

    # vtkFlyingEdges3D和vtkMarchingCubes都是VTK库中用于提取等值面的类。
    try:
        brain_extractor = vtkFlyingEdges3D()
    except AttributeError:
        brain_extractor = vtkMarchingCubes()

    # 皮肤提取器将提取出数据中值为500的等值面。
    brain_extractor.SetInputConnection(reader.GetOutputPort())
    # 第一个参数是等值面的索引。在大多数情况下，你只需要一个等值面，所以这个值通常为0。
    # 第二个参数是等值面的值。这个值表示你想要提取的等值面在标量场中的值。
    brain_extractor.SetValue(0, 70)
    # 创建皮肤的映射器
    brain_mapper = vtkPolyDataMapper()
    brain_mapper.SetInputConnection(brain_extractor.GetOutputPort())
    # 关闭了标量可见性。在VTK中，标量可见性决定了是否使用标量数据来颜色化对象。
    # 如果标量可见性被关闭，那么对象将被渲染为单一颜色。
    # 在这个例子中，关闭标量可见性意味着皮肤将被渲染为单一颜色，而不是根据标量数据变化颜色。
    brain_mapper.ScalarVisibilityOff()

    # 创建皮肤的actor，设置颜色和背面属性。
    brain = vtkActor()
    brain.SetMapper(brain_mapper)
    brain.GetProperty().SetDiffuseColor(colors.GetColor3d('SkinColor'))
    # 设置了back_prop的颜色
    back_prop = vtkProperty()
    back_prop.SetDiffuseColor(colors.GetColor3d('BackfaceColor'))
    # 将back_prop设置为皮肤对象的背面属性。在VTK中，每个对象都有前面和背面，这两个面可以有不同的属性。
    brain.SetBackfaceProperty(back_prop)

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
    a_renderer.AddActor(brain)
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


import SimpleITK as sitk

if __name__ == '__main__':
    # 调用函数
    main()
    # Read the .nii.gz file
    # image = sitk.ReadImage('T1.nii.gz')
    # numpy_array = sitk.GetArrayFromImage(image)
    # print(np.min(numpy_array), np.max(numpy_array))
