import vtk

# 自定义右键点击事件
def right_click(obj, ev):
    print("点击右键")


arrow = vtk.vtkArrowSource()
# sphere = vtk.vtkSphereSource()

arrowMapper = vtk.vtkPolyDataMapper()
arrowMapper.SetInputConnection(arrow.GetOutputPort())
arrowActor = vtk.vtkActor()
arrowActor.SetMapper(arrowMapper)


renderer = vtk.vtkRenderer()
renderer.AddActor(arrowActor)
renderer.SetBackground(0.1, 0.2, 0.4)
renderer.SetBackground2(1.0, 1.0, 1.0)
renderer.SetGradientBackground(1)

reWin = vtk.vtkRenderWindow()
reWin.AddRenderer(renderer)
reWin.SetSize(1200, 1200)

i_ren = vtk.vtkRenderWindowInteractor()
i_ren.SetRenderWindow(reWin)
# 先移除之前的右键点击事件（缩放）
i_ren.RemoveObservers('RightButtonPressEvent')
# 绑定新的右键点击事件
i_ren.AddObserver('RightButtonPressEvent', right_click)
i_ren.Initialize()
i_ren.Start()
