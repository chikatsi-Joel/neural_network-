from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget

class barre_(QWidget) :
    def __init__(self, parent : QWidget | None = None) :
        super().__init__(parent)
        
        self.central = QVBoxLayout(self)
        self.barre = QPushButton("***")
        self.butt = {
            "Profil" : QPushButton(),
            "Home" : QPushButton(),
            "Message" : QPushButton(),
            "Notif" : QPushButton(),
            "Settings" : QPushButton()
        }

        self.central.addWidget(self.barre, 0, Qt.AlignmentFlag.AlignRight)
        self.setObjectName("prox")
        [self.central.addWidget(val) for val in list(self.butt.values())[:-1]]
        self.central.addStretch(), self.central.addWidget(list(self.butt.values())[-1])
        self.setMinimumSize(QSize(80, 80))

        self.barre.setFixedSize(QSize(50, 50))

        self.init()
        self.setStyleSheet(
            """
                QPushButton{
                    border: none;
                }

                QPushButton:hover{
                    border: 1px solid grey;
                }
                #prox{
                    border: 1px solid grey;
                }
                #prox:hover{
                    border: 2px solid grey;
                }
                #prox{
                    background-color: rgb(0, 66, 94);
                }
            """
        )

    def init(self) :

        for path, (val, widg) in zip(["logo.png", "srt.png", "phone.png", "you.png", "warning.png"], list(self.butt.items())) :
            widg.setMinimumSize(QSize(50, 50))
            widg.setMaximumSize(QSize(250, 50))
            widg.setIconSize(QSize(45, 45))
            widg.setIcon(QIcon(path))
    
    def set_name_profil(self) :

        for val, widg in self.butt.items() :
            widg.setText(val)
            

    def delete_all(self) :
        for widg in self.butt.values() :
            widg.setText("")

class main(QWidget) :
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.central = QHBoxLayout(self)
        self.container = QWidget()

        self._posii = 80

        self.container.setGeometry(QRect(0, 0, 1000, 600))

        self.barre  = barre_(self.container)
        self.barre.setGeometry(QRect(0, 0, 80, 600))

        self.animation = QPropertyAnimation(self.barre, b"pos", self.container)

        self.central.addWidget(self.container)

        self.barre.barre.clicked.connect(self.start_anim_go)

        self.setFixedSize(QSize(1020, 620))

    def slotsc(self) :
        self._posii = 250


    def start_anim_go(self) :
        print("ok")
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.Type.SineCurve)
        self.animation.setStartValue(QRect(0, 0, 80, 600))
        self.animation.setEndValue(QRect(0, 0, 250, 600))

        self.animation.start()
        self.barre.set_name_profil()


import sys
app = QApplication(sys.argv)

ui = main()
ui.show()
app.exec()

sys.exit()