# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderer
)
"""
介绍如何在一个Renderwindow中使用多个Renderer。
在Step1中有提到，在一个Renderwindow中可以同时显示多个Renderer，简单来说就是一个渲染窗口中可以显示一个或多个不同的场景。
可以想象一下3DSlicer、Rhino等等从三视图的角度同时观察同一个模型的情况，大概是这个意思。
"""


def main(argv):
    colors = vtkNamedColors()

    #
    # 创建一个vtkConeSource的实例，并设置一些属性。
    #
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    #
    # 在这个例子中，用一个映射器处理对象终止管道。
    # （中间过滤器，如vtkShrinkPolyData，可以插入源和映射器之间。）
    # 创建一个vtkPolyDataMapper的实例，将多边形数据映射到图形基元。我们将锥源的输出连接到这个映射器的输入。
    #
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    #
    # 创建一个代表锥体的演员。演员协调渲染映射器的图形基元。
    # 演员还通过vtkProperty实例引用属性，并包括一个内部转换矩阵。
    # 我们将这个演员的映射器设置为我们上面创建的coneMapper。
    #
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    #
    # 创建两个渲染器并将演员分配给它们。渲染器渲染到vtkRenderWindow中的一个视口。
    # 它是屏幕上的一个窗口的一部分或全部，并且它负责绘制它拥有的演员。我们还在这里设置背景颜色。
    # 在这个例子中，我们将同一个演员添加到两个不同的渲染器中，也可以将不同的演员添加到不同的渲染器中。
    #
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('RoyalBlue'))
    # SetViewport设定视窗大小在窗口的相对位置。参数分别是左下角和右上角的坐标。
    ren1.SetViewport(0.0, 0.0, 0.5, 1.0)

    ren2 = vtkRenderer()
    ren2.AddActor(coneActor)
    ren2.SetBackground(colors.GetColor3d('DodgerBlue'))
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)

    #
    # 最后我们创建将显示在屏幕上的渲染窗口。
    # 我们使用AddRenderer将我们的渲染器放入渲染窗口。我们还设置大小为300像素乘以300。
    #
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)
    renWin.SetWindowName('Tutorial_Step3')

    #
    # 使一个视图从另一个视图看是90度。
    #
    ren1.ResetCamera()
    ren1.GetActiveCamera().Azimuth(90)

    #
    # 现在我们循环360度，并在每次渲染锥体。
    #
    for i in range(0, 360):  # 渲染图像
        renWin.Render()
        # 旋转主动相机1度
        ren1.GetActiveCamera().Azimuth(1)
        ren2.GetActiveCamera().Azimuth(1)


if __name__ == '__main__':
    import sys

    main(sys.argv)