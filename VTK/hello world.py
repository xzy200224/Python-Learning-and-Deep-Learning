# This simple example shows how to do basic rendering and pipeline
# creation.

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    # vtkNamedColors对象。Set the background color.
    colors = vtkNamedColors()
    bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
    colors.SetColor("BkgColor", *bkg)

    # 八个圆周小平面的多边形圆柱体模型。
    cylinder = vtkCylinderSource()
    cylinder.SetResolution(8)

    # 映射器负责将几何图形输入到图形库。如果定义了标量或其他属性，它也可以进行颜色映射
    cylinderMapper = vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # actor是一种分组机制：除了几何体（映射器）之外，它还具有属性、变换矩阵和/或纹理贴图。
    # 在这里，我们设置它的颜色并将其旋转22.5度
    cylinderActor = vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # 创建图形结构。渲染器渲染到渲染窗口中。
    # 渲染窗口交互程序捕获鼠标事件，并将根据事件的性质执行适当的摄影机或演员操作。
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # 将actor添加到渲染器中，设置背景和大小
    ren.AddActor(cylinderActor)
    ren.SetBackground(colors.GetColor3d("BkgColor"))
    renWin.SetSize(300, 300)
    renWin.SetWindowName('CylinderExample')

    # 允许交互程序初始化自己。必须在事件循环之前调用它。
    iren.Initialize()

    # 通过访问相机并调用“缩放”方法来放大一点。
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1.5)
    renWin.Render()

    # 启动事件循环
    iren.Start()


if __name__ == '__main__':
    main()