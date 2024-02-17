import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import vtkBoxWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
"""
此示例介绍 3D 小部件。3D 小部件利用了之前介绍的事件/观察者设计模式。
它们通常在场景中具有特定的表示，可以使用鼠标和键盘交互地选择和操作。
当控件被操作时，它们依次调用 StartInteractionEvent、InteractionEvent 和 EndInteractionEvent 等事件，这些事件可用于操作控件嵌入的场景。
3D 控件在事件循环的上下文中工作，该事件循环是在前面的例子。
"""

def main(argv):
    colors = vtkNamedColors()

    #
    # 创建一个vtkConeSource的实例，并设置一些属性。
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
    renWin.SetWindowName('Tutorial_Step6')

    #
    # vtkRenderWindowInteractor类监视vtkRenderWindow中的事件（例如，按键，鼠标）。这些事件被转化为VTK理解的事件调用（参见VTK/Common/vtkCommand.h
    # 了解VTK处理的所有事件）。然后，这些VTK事件的观察者可以适当地处理它们。
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
    # 在这里我们使用一个vtkBoxWidget来转换底层的coneActor（通过操作它的转换矩阵）。还有许多其他类型的小部件可供使用，具体请参阅文档。
    #
    # vtkBoxWidget是VTK库中的一个3D交互小部件，可以用来在3D场景中选择和操作对象。
    boxWidget = vtkBoxWidget()
    # 将vtkBoxWidget与一个vtkRenderWindowInteractor实例关联起来
    boxWidget.SetInteractor(iren)
    # 设置了vtkBoxWidget相对于其输入数据的边界框的初始大小
    boxWidget.SetPlaceFactor(1.25)
    # 设置了vtkBoxWidget的轮廓颜色为金色
    boxWidget.GetOutlineProperty().SetColor(colors.GetColor3d('Gold'))

    #
    # 初始放置交互器。3D小部件的输入用于最初定位和缩放小部件。观察到EndInteractionEvent，它调用SelectPolygons回调。
    #
    # 将vtkBoxWidget与一个3D对象（这里是coneActor）关联起来。
    # 这样，当vtkBoxWidget发生变换时，这个变换会被应用到关联的3D对象上，从而改变3D对象的位置、旋转和缩放等属性。
    boxWidget.SetProp3D(coneActor)
    # 将vtkBoxWidget放置在其关联的3D对象的位置。
    boxWidget.PlaceWidget()
    # vtkMyCallback的__call__方法被设计为响应vtkBoxWidget的交互事件。
    callback = vtkMyCallback()
    # 当vtkBoxWidget发生'InteractionEvent'事件时，callback会被调用，从而实现对vtkBoxWidget的交互事件的响应
    boxWidget.AddObserver('InteractionEvent', callback)

    #
    # 通常，用户按下'i'键来激活一个3D小部件。在这里，我们将手动启用它，使其与锥体一起出现。
    #
    boxWidget.On()

    #
    # 开始事件循环。
    #
    iren.Initialize()
    iren.Start()

class vtkMyCallback(object):
    """
    交互的回调。
    实时地改变3D对象的位置、旋转和缩放等属性。
    """
    def __call__(self, caller, ev):
        # 创建了一个vtkTransform对象t
        t = vtkTransform()
        # 然后从caller（即vtkBoxWidget的实例）中获取当前的变换，并将其存储在t中
        widget = caller
        widget.GetTransform(t)
        # 这个变换被应用到vtkBoxWidget关联的3D对象（通过GetProp3D()获取
        widget.GetProp3D().SetUserTransform(t)


if __name__ == '__main__':
    import sys

    main(sys.argv)