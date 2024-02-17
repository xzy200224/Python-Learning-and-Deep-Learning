import vtk

canvas =vtk.vtkImageCanvasSource2D()
canvas.SetScalarTypeToUnsignedChar()
canvas.SetNumberOfScalarComponents(1)
canvas.SetExtent(0,100,0,100,0,0)
canvas.SetDrawColor(0,0,0,0)
canvas.FillBox(0,100,0,100)

canvas.SetDrawColor(255,0,0,0)
canvas.FillBox(20,40,20,40)

canvas.Update()

image_data = canvas.GetOutput()

# 演员
actor = vtk.vtkImageActor()
# 演员添加映射器
actor.SetInputData(image_data)
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
