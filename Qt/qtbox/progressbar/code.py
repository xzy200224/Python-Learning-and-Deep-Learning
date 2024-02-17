from PyQt5.QtWidgets import QProgressBar


class QtBoxStyleProgressBar2(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar2, self).__init__()
        self.setTextVisible(False)
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 2px solid #888783;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #74d65f;
            border-radius: 2px;
            width: 9px;
            margin: 0.5px;
        }
        """)
        """
        QProgressBar {
            border: 2px solid white;
            background-color: black;
            padding-left: 2px;
            padding-right: 2px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: white;
            margin-top: 2px;
            margin-bottom: 2px;
        }
        """
