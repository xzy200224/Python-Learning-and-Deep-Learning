from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QApplication, QWidget, QVBoxLayout
import sys
from qfluentwidgets import TreeWidget

class Recon_all_tree_2(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.tree = TreeWidget(self)
        self.tree.setHeaderHidden(True)
        self.tree.setColumnCount(1)
        # 设置1列，隐藏header
        self.create_items()

    def create_items(self):
        # 设置顶部项目
        top_level_items = ['autorecon1', 'autorecon2', 'autorecon3']
        for i, top_level_item in enumerate(top_level_items):
            item = QTreeWidgetItem(self.tree, [top_level_item])
            item.setFlags(item.flags() | Qt.ItemIsAutoTristate | Qt.ItemIsUserCheckable)
            item.setCheckState(0, Qt.Unchecked)
            if i == 0:
                child_items = ['Motion Correction and Conform', 'NU (Non-Uniform intensity normalization)', 'Talairach transform computation', 'Intensity Normalization 1', 'Skull Strip']
            elif i == 1:
                child_items = ['EM Register (linear volumetric registration)', 'CA Intensity Normalization', 'CA Non-linear Volumetric Registration', 'Remove Neck', 'LTA with Skull', 'CA Label (Volumetric Labeling, ie Aseg) and Statistics', 'Intensity Normalization 2 (start here for control points)', 'White matter segmentation', 'Edit WM With ASeg', 'Fill (start here for wm edits)', 'Tessellation (begins per-hemisphere operations)', 'Smooth1', 'Inflate1', 'QSphere', 'Automatic Topology Fixer', 'Final Surfs (start here for brain edits for pial surf)', 'Smooth2', 'Inflate2']
            elif i == 2:
                child_items = ['Spherical Mapping', 'Spherical Registration', 'Spherical Registration, Contralateral hemisphere', 'Map average curvature to subject', 'Cortical Parcellation - Desikan_Killiany and Christophe (Labeling)', 'Cortical Parcellation Statistics', 'Cortical Ribbon Mask', 'Cortical Parcellation']
            # 设置子项目
            for j, child_item in enumerate(child_items):
                item_child = QTreeWidgetItem(item, [child_item])
                item_child.setFlags(item_child.flags() | Qt.ItemIsAutoTristate | Qt.ItemIsUserCheckable)
                item_child.setCheckState(0, Qt.Unchecked)

        # 创建布局管理器并设置为MyTreeWidget的布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Recon_all_tree_2()
    win.show()
    app.exec()

