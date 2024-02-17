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
创建一个多边形棱锥显示在屏幕中，并使相机围绕棱锥进行360°旋转，随后退出窗口。
"""
def main(argv):
    #
    # 创建vtkNamedColors实例，用于选择对象和背景的颜色
    #
    colors = vtkNamedColors()

    #
    # 创建vtkConeSource实例并设定一些属性，
    # 该source实例通过本地参数生成棱锥模型数据。
    # VtkConeSource实例“cone”是可视化pipeline的一部分。
    # 它生成一些其它filter也许会处理的数据（输出vtkPolyData类型数据）。
    #
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)
    #
    # 在示例中，我们使用mapper进程对象来结束pipeline。
    # (中间的filter比如vtkShrinkPolyData也许会被插入到source和mapper之间)
    # 我们创建一个实例化的vtkPolyDataMapper去将多边形数据映射到基本图形层中。
    # 我们将cone source连接到这个mapper的输入
    #
    coneMapper = vtkPolyDataMapper()  # vtkPolyDataMapper将多边形数据比如vtkPolyData映射到基本图形层中。
    coneMapper.SetInputConnection(
        cone.GetOutputPort())  # SetInputConnection为给定的输入端口索引设置连接，其输入是另一个filter的输出端口，通过GetOutputPort获得。
    #
    # 创建一个actor代表cone。actor策划mapper基本图形层的渲染。
    # 一个actor也通过vtkProperty实例化来改变属性，并包括了一个内部变换矩阵。我们设定之前创建的这个actor的mapper为“coneMapper”。
    #
    coneActor = vtkActor()  # 代表了一个渲染场景中的一个对象（几何图形及属性），vtkActor用于表示渲染场景中的实体，它继承了vtkProp的actors位姿相关函数。
    coneActor.SetMapper(coneMapper)  # 连接一个actor到一个可视化pipeline的结尾（比如mapper）
    coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))
    #
    # 创建一个Renderer并将actors分配进去。一个renderer就像一个视窗，是屏幕中的一个或者部分窗口，用于绘制它拥有的actors。我们也在这里设定背景色。
    #
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('MidnightBlue'))

    # 最终我们创建render窗口，它将显示在屏幕中。我们使用AddRenderer将renderer放在render窗口中。我们也将尺寸设定在300*300像素大小。
    #
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300, 300)
    renWin.SetWindowName('Tutorial_Step1')

    #
    # 现在我们循环360°，并在每一刻渲染cone。
    #
    for i in range(0, 360):
        # 渲染图像
        renWin.Render()
        # 旋转相机1°，注意：Azimuth是旋转相机的操作，
        # 它将使相机绕着以焦点为中心，view up方向的轴进行角度旋转，而模型不动。
        # 其中view up方向是人为设定的，在世界坐标系下的相机坐标系的Y轴方向（在官方文档中vtkcamera类中的函数中有说明）。
        # 关于这部分我也许会在后续相机部分进行介绍（如果有需要的话）。
        ren1.GetActiveCamera().Azimuth(1)


if __name__ == '__main__':
    import sys

    main(sys.argv)