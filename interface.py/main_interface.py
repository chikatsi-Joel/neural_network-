from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import *


class login_form(QLabel) :
    def __init__(self, parent : QWidget | None = None) :
        super(login_form, self).__init__(parent)
        self.central = QVBoxLayout(self)
        self.grid = QGridLayout()
        self.title = QLabel("Login")

        self.name = QLabel("Name : ")
        self.name.setObjectName("name")
        self.name_edit = QLineEdit()

        self.email = QLabel("Email : ")
        self.email.setObjectName("email")
        self.email_edit = QLineEdit()

        self.close_butt = PrimaryToolButton(FluentIcon.CLOSE)
        self.link = HyperlinkButton("", "Log in", parent = self)
        self.valider = PrimaryPushButton("Valider")


        font = QFont()
        font.setFamily("ori1Uni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(0, 128, 137);")

        self.name_edit.setFixedHeight(40), self.email_edit.setFixedHeight(40)
        self.name_edit.setFont(font := QFont("Yrsa Regular")), self.email_edit.setFont(font)
        font.setFamily("Sans")

        
        self.central.addWidget(self.close_butt, alignment = Qt.AlignmentFlag.AlignRight)
        self.central.addWidget(self.title, alignment= Qt.AlignmentFlag.AlignHCenter)
        self.central.addLayout(self.grid)

        #self.central.addSpacerItem(QSpacerItem(30, 100))
        self.setStyleSheet(open("st.css", 'r').read())

        self.grid.addWidget(self.name, 0, 0), self.grid.addWidget(self.name_edit, 0, 1)
        self.grid.addItem(QSpacerItem(30, 10), 1, 0)
        self.grid.addWidget(self.email, 2, 0), self.grid.addWidget(self.email_edit, 2, 1)
        self.grid.addItem(QSpacerItem(30, 10), 3, 0)
        self.grid.addWidget(self.valider, 4, 1)
        self.central.addSpacerItem(QSpacerItem(30, 30))

        self.central.addWidget(self.link)

        self.setObjectName("log")



class login_page(QLabel) :
    def __init__(self, parent: QWidget | None = None) -> None:
        super(login_page, self).__init__(parent)

        self.central = QVBoxLayout(self)

        self.icon = ImageLabel("logo.png")
        self.title = QLabel("Processing Movie")

        self.icon.setScaledContents(True)
        self.icon.setBorderRadius(10, 5, 10, 5)
        self.icon.setFixedSize(QSize(300, 300))

        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        font = QFont()
        font.setFamily("ori1Uni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: white;")

        self.central.addWidget(self.title, alignment = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.setObjectName("login_pager")
        self.setStyleSheet(
            """
            QLabel{
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(75, 202, 252, 255), stop:1 rgba(0, 128, 137, 230));
                border-top-right-radius: 20px;
                border-bottom-left-radius: 20px;
            }
            """
        )

    def paintEvent(self, a0: QPaintEvent | None) -> None:

        return super().paintEvent(a0)
        



class main(QMainWindow) :
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.container = QWidget(self)

        self.login_page = login_page(self.container)
        self.login_form = login_form(self.container)


        self.container.setGeometry(QRect(20, 20, 650, 1000))

        self.animation = QPropertyAnimation(self.login_form, b"geometry", self)
        self.animation.setStartValue(QRect(0, 0, 0, 0))
        self.animation.setEndValue(QRect(489, 80, 400, 480))
        self.animation.setEasingCurve(QEasingCurve.Type.OutElastic)

        """effect = QGraphicsOpacityEffect(self.logo)
        self.logo.setGraphicsEffect(effect)
        animation_opacity = QPropertyAnimation(effect, b"opacity", self)
        animation_opacity.setStartValue(0)
        animation_opacity.setEndValue(1)
        animation_opacity.setDuration(2000)"""


        self.animation_1 = QPropertyAnimation(self.login_page, b"geometry", self)
        self.animation_1.setStartValue(QRect(650, 0, 0, 0))
        self.animation_1.setEndValue(QRect(10, 20, 480, 600))
        self.animation_1.setEasingCurve(QEasingCurve.Type.OutElastic)

        self.animation_1.setDuration(2000)
        self.animation_1.start()

        self.animation.setDuration(2000)

        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(self.animation)
        #self.animation_group.addAnimation(animation_opacity)
        self.animation_group.start()
        
        self.login_form.valider.installEventFilter(ToolTipFilter(self.login_form.valider, 0, ToolTipPosition.TOP))
    
        self.setFixedSize(QSize(1300, 655))

        self.setCentralWidget(self.container)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setFixedSize(QSize(900, 650))
        
        self.login_form.close_butt.clicked.connect(lambda: self.close())
        self.login_form.valider.clicked.connect(self.going_form)
        self.center()


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        widget_size = self.geometry()
        self.move((screen.width() - widget_size.width()) // 2, (screen.height() - widget_size.height()) // 2) 

    def going_form(self) :
        self.animation_1 = QPropertyAnimation(self.login_form, b"geometry", self)
        self.animation_1.setDuration(2000)
        self.animation_1.setEasingCurve(QEasingCurve.Type.SineCurve)
        self.animation_1.setStartValue(QRect(480, 80, 400, 480))
        self.animation_1.setEndValue(QRect(650, 0, 0, 0))
        self.animation_1.start()





import sys
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
app = QApplication(sys.argv)

form = QWidget()
ui = main()
ui.show()
app.exec()

sys.exit()