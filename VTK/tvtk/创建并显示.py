from tvtk.api import tvtk
"""
三维对象:
CubeSource-立方体
ConeSource-圆锥体
CylinderSource-圆柱体
ArcSource-圆弧
ArrowSource-箭头

对象方法：
set/get_x_length()
set/get_y_length()
set/get_z_length()
set/get_center()
set/get_bounds()

属性：
s.x_length
s.y_length
s.z_length
s.center
"""
# 创建一个立方体数据源并设置长宽高
s =  tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# 使用PolyDataMapper（映射器）将数据源对象映射为图形数据
m = tvtk.PolyDataMapper(input_connection=s.output_port)
# 创建一个Actor（实体）将图形数据映射为图形
a = tvtk.Actor(mapper=m)
# 创建一个Renderer（渲染器）将Actor添加进去
ren = tvtk.Renderer(background=(0, 0, 0))
ren.add_actor(a)
# 创建一个RenderWindow将Renderer添加进去
ren_win = tvtk.RenderWindow(size=(300, 300))
ren_win.add_renderer(ren)
#  创建一个RenderWindowInteractor（窗口交互工具）将RenderWindow添加进去
iren = tvtk.RenderWindowInteractor(render_window=ren_win)
# 开启交互
iren.initialize()
iren.start()