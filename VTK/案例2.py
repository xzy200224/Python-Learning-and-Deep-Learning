import vtk
# VTK
# 数据源 resource:
cone = vtk.vtkConeSource()
# 映射器 mapper：
coneMapper = vtk.vtkPolyDataMapper()
# 映射器添加数据源：
coneMapper.SetInputConnection( cone.GetOutputPort() )
# 演员 actor:
coneActor = vtk.vtkActor()
# 演员添加映射器：
coneActor.SetMapper( coneMapper )
# 绘制器 renderer:
renderer = vtk.vtkRenderer()
# 绘制器添加演员：
renderer.AddActor( coneActor )
# 绘制窗口 win：
renWin = vtk.vtkRenderWindow()
# 绘制窗口添加绘制器：
renWin.AddRenderer( renderer )
# 窗口读取绘制器生成的图形：
renWin.Render()
# 交互器 i_ren:
i_ren = vtk.vtkRenderWindowInteractor()
# 交互器添加渲染窗口
i_ren.SetRenderWindow(renWin)
# 交互器初始化：
i_ren.Initialize()
# 交互器开启；
i_ren.Start()
