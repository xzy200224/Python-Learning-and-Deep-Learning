import vtk

# *******三个点 加拓扑*******
# 创建点数据
points = vtk.vtkPoints()
# 创建顶点类型
vertices = vtk.vtkCellArray()

# 创建点的坐标
points_list = [[1,0,0],[0,0,1],[0,0,0]]

for point in points_list:
    # 每个点坐标加入到 vtkPoints 中，返回加入点的索引号
    id = points.InsertNextPoint(point)
    # 在每个坐标点上分别创建一个顶点，顶点是单元 Cell 里的一种类型
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(id)

line0 = vtk.vtkLine()
line0.GetPointIds().SetId(0,0)
line0.GetPointIds().SetId(1,1)

line1 = vtk.vtkLine()
line1.GetPointIds().SetId(0,1)
line1.GetPointIds().SetId(1,2)

line2 = vtk.vtkLine()
line2.GetPointIds().SetId(0,2)
line2.GetPointIds().SetId(1,0)

lines = vtk.vtkCellArray()
lines.InsertNextCell(line0)
lines.InsertNextCell(line1)
lines.InsertNextCell(line2)

# 创建 vtkPolyData 对象
polydata = vtk.vtkPolyData()
# 指定数据集的几何结构（由 points 指定）
polydata.SetPoints(points)
# 指定数据集的拓扑结构（由 vertices 指定）
polydata.SetVerts(vertices)

polydata.SetLines(lines)


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

actor.GetProperty().SetPointSize(10)
actor.GetProperty().SetLineWidth(10)

render = vtk.vtkRenderer()
render.SetBackground(0, 0, 0)

# Renderer Window
window = vtk.vtkRenderWindow()
window.AddRenderer(render)
window.SetSize(600, 600)

# System Event
win_render = vtk.vtkRenderWindowInteractor()
win_render.SetRenderWindow(window)

# Style
win_render.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())

# Insert Actor
render.AddActor(actor)

win_render.Initialize()
win_render.Start()

