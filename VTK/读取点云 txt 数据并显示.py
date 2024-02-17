import numpy
import vtk
from vtk.util.numpy_support import numpy_to_vtk


def data_actor(source_data):
    # 新建 vtkPoints 实例
    points = vtk.vtkPoints()
    # 导入点数据
    points.SetData(numpy_to_vtk(source_data))
    # 新建 vtkPolyData 实例
    polydata = vtk.vtkPolyData()
    # 设置点坐标
    polydata.SetPoints(points)

    # 顶点相关的 filter
    vertex = vtk.vtkVertexGlyphFilter()
    vertex.SetInputData(polydata)

    # mapper 实例
    mapper = vtk.vtkPolyDataMapper()
    # 关联 filter 输出
    mapper.SetInputConnection(vertex.GetOutputPort())

    # actor 实例
    actor = vtk.vtkActor()
    # 关联 mapper
    actor.SetMapper(mapper)

    # 红色点显示
    #actor.GetProperty().SetColor(1,0,0)
    return actor


def data_actor_transform(source_data):
    # 新建 vtkPoints 实例
    points = vtk.vtkPoints()
    # 导入点数据
    points.SetData(numpy_to_vtk(source_data))
    # 新建 vtkPolyData 实例
    polydata = vtk.vtkPolyData()
    # 设置点坐标
    polydata.SetPoints(points)

    # 顶点相关的 filter
    vertex = vtk.vtkVertexGlyphFilter()
    vertex.SetInputData(polydata)

    # 设置变换过程
    transform = vtk.vtkTransform()
    transform.Translate(0,0,0)
    transform.RotateY(180)
    # 新建变换的 filter
    transformFilter = vtk.vtkTransformPolyDataFilter()
    # 将变换 filter 输入设置为点数据模型
    transformFilter.SetInputConnection(vertex.GetOutputPort())
    # 设置变换过程
    transformFilter.SetTransform(transform)
    transformFilter.Update()



    # mapper 实例
    mapper = vtk.vtkPolyDataMapper()
    # 关联 filter 输出
    mapper.SetInputConnection(transformFilter.GetOutputPort())

    # actor 实例
    actor = vtk.vtkActor()
    # 关联 mapper
    actor.SetMapper(mapper)

    # 红色点显示
    #actor.GetProperty().SetColor(1,0,0)
    return actor


def show_actor(actor_list):
    # render
    render = vtk.vtkRenderer()
    render.SetBackground(0, 0, 0)

    # Renderer Window
    window = vtk.vtkRenderWindow()
    window.AddRenderer(render)
    window.SetSize(1200, 1200)

    # System Event
    win_render = vtk.vtkRenderWindowInteractor()
    win_render.SetRenderWindow(window)

    # Style
    win_render.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())

    # Insert Actor
    for actor in actor_list:
        render.AddActor(actor)
    win_render.Initialize()
    win_render.Start()


if __name__ == '__main__':
    # 读取 txt 文档
    source_data1 = numpy.loadtxt("bun000.txt")
    source_data2 = numpy.loadtxt("bun180.txt")

    actor1 = data_actor(source_data1)
    actor2 = data_actor_transform(source_data2)
    actor2.GetProperty().SetColor(1, 0, 0)

    actor_list = [actor1,actor2]
    show_actor(actor_list)
