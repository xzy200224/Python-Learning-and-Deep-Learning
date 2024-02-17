from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication
import sys

class Recon_all_tree(QTreeWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        # 设置1列，隐藏header
        self.setColumnCount(1)
        self.setHeaderHidden(True)
        self.create_items()

    def create_items(self):
        # 设置顶部项目
        top_level_items = ['autorecon1', 'autorecon2', 'autorecon3']
        for i, top_level_item in enumerate(top_level_items):
            item = QTreeWidgetItem(self, [top_level_item])
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

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = Recon_all_tree()
#     win.show()
#     app.exec()
