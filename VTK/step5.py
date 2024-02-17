import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
"""
这个例子将交互的概念引入了python环境(vtkrenderinteractor），即鼠标或键盘与渲染窗口中模型的交互。
比如通过鼠标进行移动、旋转、缩放等操作。该示例定义了一种与默认样式(vtkInteractorStyle)不同的交互样式：
vtkInteractorStyleTrackballCamera。默认风格中，按键j和t可以切换joystic(位置感应)和trackball(运动感应)风格，
在joystic风格中只要鼠标按键就会发生连续的运动。在tracball风格中鼠标按键并挪动指针才会发生运动。
按键c和a在相机模式和actor模式中切换，相机模式下鼠标事件会影响相机的位置和焦点，actor模式下鼠标事件影响位于鼠标指针下的actor。

vtkInteractorStyleTrackballCamera的交互风格通过交互实现操纵场景中的相机、场景的视点。
在trackball交互中，鼠标运动的幅度与鼠标绑定相关的camera运动成正比。
例如，按住左键进行小幅度运动会导致相机在焦点周围的旋转发生细微的变化。
对于三键鼠标，左键用于旋转，右键用于缩放，中键用于平移，ctrl+左键用于旋转，shift+右键用于快速旋转，
shift+右键用于环境旋转（鼠标按键较少时，shift+左键用于平移）。还有很多交互风格可以在官网中进行了解。
"""

def main(argv):
    colors = vtkNamedColors()

    #
    # 接下来我们创建一个vtkConeSource的实例，并设置一些属性。
    # vtkConeSource 'cone'的实例是一个可视化管道的一部分（它是一个源处理对象），它产生数据（输出类型是vtkPolyData），其他过滤器可能会处理这些数据。
    #
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    #
    # 在这个例子中，我们用一个映射器处理对象终止管道。
    # （中间过滤器，如vtkShrinkPolyData，可以插入源和映射器之间。）
    # 我们创建一个vtkPolyDataMapper的实例，将多边形数据映射到图形基元。我们将锥源的输出连接到这个映射器的输入。
    #
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    #
    # 创建一个代表锥体的演员。演员协调渲染映射器的图形基元。演员也通过vtkProperty实例引用属性，并包括一个内部转换矩阵。我们将这个演员的映射器设置为我们上面创建的coneMapper。
    #
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('Bisque'))

    #
    # 创建渲染器并将演员分配给它。渲染器就像一个视口。它是屏幕上的一个窗口的一部分或全部，并且它负责绘制它拥有的演员。我们也在这里设置背景颜色。
    #
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('MidnightBlue'))

    #
    # 最后我们创建将显示在屏幕上的渲染窗口。
    # 我们使用AddRenderer将我们的渲染器放入渲染窗口。我们也设置大小为300像素乘以300。
    #
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300, 300)
    renWin.SetWindowName('Tutorial_Step5')

    #
    # vtkRenderWindowInteractor类监视vtkRenderWindow中的事件（例如，按键，鼠标）。这些事件被转化为VTK理解的事件调用（参见VTK/Common/vtkCommand.h
    # 了解VTK处理的所有事件）。然后，这些VTK事件的观察者可以适当地处理它们。
    # vtkRenderWindowInteractor类在vtkRenderWindow中观察events(比如键盘按键或者鼠标)这些events被译成VTK可以理解的事件调用中。
    # 然后这些VTK events的observers可以适当地进行处理
    #
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    #
    # 默认情况下，vtkRenderWindowInteractor实例化一个vtkInteractorStyle实例。
    # vtkInteractorStyle将它观察到的一组事件转化为在vtkRenderWindowInteractor关联的vtkRenderWindow上的相机、演员和/或属性的操作。
    # 在这里我们指定一个特定的交互样式。
    #
    style = vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    #
    # 与前面的脚本不同，我们在这里执行了一些操作然后退出，这里我们保留一个事件循环运行。用户可以使用鼠标和键盘根据当前的交互样式在场景上执行操作。
    # 当用户按下'e'键时，默认情况下，vtkRenderWindowInteractor会调用一个ExitEvent，这被捕获并退出事件循环（由下面的Start()方法触发）。
    #
    iren.Initialize()
    iren.Start()

    #
    # 最后注意：回忆一下观察者可以观察特定的事件并采取适当的行动。在渲染窗口中按'u'会导致vtkRenderWindowInteractor调用一个UserEvent。
    # 这可以被捕获以弹出一个GUI等。参见Tcl Cone5.tcl示例了解这是如何工作的。


if __name__ == '__main__':
    import sys

    main(sys.argv)