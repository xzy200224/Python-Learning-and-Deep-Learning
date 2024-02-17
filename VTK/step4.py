import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderer
)


def main(argv):
    colors = vtkNamedColors()

    #
    # 接下来我们创建一个vtkConeSource的实例，并设置一些属性。
    # vtkConeSource "cone"的实例是一个可视化管道的一部分（它是一个源处理对象），它产生数据（输出类型是vtkPolyData），其他过滤器可能会处理这些数据。
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
    # 创建一个代表第一个锥体的演员。修改演员的属性以赋予其不同的表面属性。
    # 默认情况下，创建一个演员会创建一个属性，所以可以使用GetProperty()方法。
    #
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    coneActor.GetProperty().SetDiffuse(0.7)
    coneActor.GetProperty().SetSpecular(0.4)
    coneActor.GetProperty().SetSpecularPower(20)

    #
    # 创建一个属性并直接操作它。将其分配给第二个演员。
    #
    property = vtkProperty()
    property.SetColor(colors.GetColor3d("Tomato"))
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)

    #
    # 创建第二个actor和一个property。
    # Property被直接设置并分配到第二个actor中。通过这种方式，一个单独的property可以被分享给多个actor。
    # 即多个acotr可以采用相同的属性配置。注意，我们使用和第一个actor相同的mapper。
    # 这个方式避免了重复的几何属性，这样可以节省很多内存（如果几何尺寸过大）
    #
    coneActor2 = vtkActor()
    coneActor2.SetMapper(coneMapper)
    coneActor2.GetProperty().SetColor(colors.GetColor3d("LightSeaGreen"))
    coneActor2.SetProperty(property)
    coneActor2.SetPosition(0, 2, 0)

    #
    # 创建渲染器并将演员分配给它。渲染器就像一个视口。它是屏幕上的一个窗口的一部分或全部，并且它负责绘制它拥有的演员。我们也在这里设置背景颜色。
    #
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.AddActor(coneActor2)
    ren1.SetBackground(colors.GetColor3d("CornflowerBlue"))

    #
    # 最后我们创建将显示在屏幕上的渲染窗口。
    # 我们使用AddRenderer将我们的渲染器放入渲染窗口。我们也设置大小为300像素乘以300。
    #
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300, 300)
    renWin.SetWindowName("Tutorial_Step4")

    #
    # 现在我们循环360度，并在每次渲染锥体。
    #
    for i in range(0, 360):  # 渲染图像
        # 渲染图像
        renWin.Render()
        # 旋转主动相机1度
        ren1.GetActiveCamera().Azimuth(1)


if __name__ == '__main__':
    import sys

    main(sys.argv)