import vtk
# 数据源：箭头
arrow_source = vtk.vtkArrowSource()
# 映射器
mapper = vtk.vtkPolyDataMapper()
# 映射器添加数据源
mapper.SetInputConnection(arrow_source.GetOutputPort())
# 演员
actor = vtk.vtkActor()
# 演员添加映射器
actor.SetMapper(mapper)
# 绘制器
ren = vtk.vtkRenderer()
# 绘制器添加演员
ren.AddActor(actor)
# 绘制窗口
renWin = vtk.vtkRenderWindow()
# 绘制窗口添加绘制器
renWin.AddRenderer(ren)
# 窗口读取绘制器生成的图形
renWin.Render()
# 创建窗口交互器
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()
