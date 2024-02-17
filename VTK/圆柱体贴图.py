import vtk

# *************柱体****************
# 生成一个中心在渲染场景原点的柱体，柱体的长轴沿着Y轴，柱体的高度、截面半径等都可以任意指定
cylinder = vtk.vtkCylinderSource()
# 高
cylinder.SetHeight(3.0)
# 截面半径
cylinder.SetRadius(1.0)
# 横截面边数
cylinder.SetResolution(360)
print(f"高:{cylinder.GetHeight()}、半径:{cylinder.GetRadius()}、面:{cylinder.GetResolution()}")
# 映射,将输入的数据转换为几何图元(点、线、多边形)进行渲染
cylinderMapper = vtk.vtkPolyDataMapper()
# 设置 VTK 可视化管线的输入数据接口，对应的可视化管线输出数据的接口为 GetOutputPort()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

# 三维空间中渲染对象最常用的 vtkProp 子类是 vtkActor(表达场景中的几何数据)和 vtkVolume(表达场景中的体数据)
"""vtkProp子类负责确定渲染场景中对象的位置、大小和方向信息。
Prop依赖于两个对象(Prop一词来源于戏剧里的“道具”，在VTK里表示的是渲染场景中可以看得到的对象。)
一个是Mapper(vtkMapper)对象，负责存放数据和渲染信息，另一个是属性(vtkProperty)对象，负责控制颜色、不透明度等参数。
"""
cylinderActor = vtk.vtkActor()
print(f"位置:{cylinderActor.GetPosition()}")

# 改变属性颜色
cylinderProperty = vtk.vtkProperty()
cylinderProperty.SetColor(0.6,0.96,1)
print("颜色:",cylinderProperty.GetColor())

# 读取 bmp 背景图片
pngReader = vtk.vtkPNGReader()
pngReader.SetFileName("屏幕截图 2024-02-09 215234.png")
# bmpReader = vtk.vtkBMPReader()
# bmpReader.SetFileName("sky.bmp")
# 纹理
texture = vtk.vtkTexture()
# 数据接口联通纹理
texture.SetInputConnection(pngReader.GetOutputPort())
# 插入纹理
texture.InterpolateOn()
# 绘制对象添加映射器，设置定义Actor几何形状的Mapper
cylinderActor.SetMapper(cylinderMapper)
# 设置Actor的属性
cylinderActor.SetProperty(cylinderProperty)
# 设置纹理属性
cylinderActor.SetTexture(texture)

# 绘制器，负责管理场景的渲染过程。
# 组成场景的所有对象包括Prop，照相机(Camera)和光照(Light)都被集中在一个vtkRenderer对象中。
# 一个vtkRenderWindow中可以有多个vtkRenderer对象，而这些vtkRenderer可以渲染在窗口中不同的矩形区域中(即视口)，或者覆盖整个窗口区域。
renderer = vtk.vtkRenderer()
# 绘制器添加对象，添加vtkProp类型的对象到渲染场景中
renderer.AddActor(cylinderActor)
# 绘制器设置背景，设置渲染场景的背景颜色
renderer.SetBackground(1.0,0.87,0.68)
print("Renderer bg:",renderer.GetBackground())
# SetBackground2()用于设置渐变的另外一种颜色
renderer.SetBackground2(1.0,1.0,1.0)
# 打开背景颜色渐变效果，相当于调用方法 GradientBackgroundOn()
renderer.SetGradientBackground(1)


# 绘制窗口,将操作系统与VTK渲染引擎连接到一起
renWin = vtk.vtkRenderWindow()
# 绘制窗口添加绘制器,加入 vtkRenderer 对象
renWin.AddRenderer(renderer)
# 设置窗口的大小，以像素为单位
renWin.SetSize(1200,1200)
print("Window size:",renWin.GetSize())
# 绘制窗口内所有绘制器同步渲染绘制
#renWin.Render()
# 交互器,提供平台独立的响应鼠标、键盘和时钟事件的交互机制
"""vtkRenderWindowInteractor自动建立一个默认的3D场景交互器样式(Interactor Style)：vtkInteractorStyleSwitch，
当然你也可以选择其他的交互器样式，或者是创建自己的交互器样式"""
i_ren = vtk.vtkRenderWindowInteractor()
# 交互器绑定绘制窗口,设置渲染窗口，消息是通过渲染窗口捕获到的，所以必须要给交互器对象设置渲染窗口
i_ren.SetRenderWindow(renWin)
# 为处理窗口事件做准备，交互器工作之前必须先调用这个方法进行初始化
i_ren.Initialize()
# 开始进入事件响应循环，交互器处于等待状态，等待用户交互事件的发生
i_ren.Start()
