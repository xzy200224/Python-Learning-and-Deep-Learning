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
创建observer用于获得step1中每次渲染时相机的位置。VTK使用command/observer设计模式。
也就是说，observer观察任何vtkObject（或子类）可能调用自身的特定事件。
例如，vtkRenderer在开始呈现时调用“StartEvent”。在这里，我们添加一个Observer，它在观察到此事件时调用command。
即触发某事件时调用回调函数。
"""
def main(argv):
    colors = vtkNamedColors()
    #
    # 这个pipeline的创建已在 Tutorial_Step1中介绍.
    #
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('MidnightBlue'))
    # 重置活动相机的位置和方向，使得所有的渲染对象都在视野中。
    ren1.ResetCamera()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300, 300)
    renWin.SetWindowName('Tutorial_Step2')

    # 我们在这里设置observer.
    mo1 = vtkMyCallback(ren1)
    # 当触发StartEvent事件时调用mo1
    ren1.AddObserver('StartEvent', mo1)

    for i in range(0, 360):
        # 渲染图像.
        renWin.Render()
        # 旋转主动相机1°
        # 获得当前相机，Azimuth将相机沿着以焦点为中心的view up vector(Y轴)向上旋转
        # 注意view up vector是通过setviewup设置的，并不一定垂直于投影的方向，其结果是相机的水平旋转（绕着焦点）。
        ren1.GetActiveCamera().Azimuth(1)


class vtkMyCallback(object):
    """
    交互的Callback
    """
    def __init__(self, renderer):
        self.renderer = renderer

    def __call__(self, caller, ev):
        # 每个渲染器（renderer）都有一个活动相机（active camera），这个相机定义了从哪个视角来查看场景。
        # self.renderer.GetActiveCamera()是获取当前渲染器的活动相机。
        # GetPosition()是获取相机在世界坐标系中的位置。这个位置是一个三维坐标（x, y, z），表示相机的位置
        position = self.renderer.GetActiveCamera().GetPosition()
        print('({:5.2f}, {:5.2f}, {:5.2f})'.format(*position))


if __name__ == '__main__':
    import sys

    main(sys.argv)