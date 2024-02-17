from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QWidget
import sys
from qfluentwidgets import TreeWidget, setTheme, Theme, TreeView

class MyTreeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tree = TreeWidget(self)
        # 添加顶级项目
        for i in range(3):
            top_level_item = QTreeWidgetItem(self.tree)
            top_level_item.setText(0, f"Top Level {i}")
            top_level_item.setFlags(top_level_item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
            top_level_item.setCheckState(0, Qt.Unchecked)
            # 添加子项目
            for j in range(3):
                child_item = QTreeWidgetItem(top_level_item)
                child_item.setText(0, f"Child {j}")
                child_item.setFlags(child_item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
                child_item.setCheckState(0, Qt.Unchecked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree_widget = MyTreeWidget()
    tree_widget.show()
    sys.exit(app.exec_())