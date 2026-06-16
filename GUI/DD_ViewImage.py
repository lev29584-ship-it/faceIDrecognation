from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from BUS.DiemDanhBUS import DiemDanhBUS


class DD_ViewImage(object):

    def __init__(self, idDD):
        self.idDD = idDD

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(350, 350)

        # ===== MAIN LAYOUT =====
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)

        # ===== IMAGE LABEL =====
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            QLabel{
                border:1px solid gray;
            }
        """)

        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)

        # load image
        self.getImage()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(
            _translate("Form", "Ảnh điểm danh")
        )

    def getImage(self):

        try:
            ddBUS = DiemDanhBUS()

            data = ddBUS.findMaDiemDanh(self.idDD)

            if not data:
                QMessageBox.warning(
                    None,
                    "Thông báo",
                    "Không tìm thấy ảnh điểm danh"
                )
                return

            link_image = None

            for row in data:
                link_image = row[0]
                break

            # check file tồn tại
            if not link_image or not os.path.exists(link_image):
                QMessageBox.warning(
                    None,
                    "Thông báo",
                    "Ảnh không tồn tại"
                )
                return

            pixmap = QPixmap(link_image)

            pixmap = pixmap.scaled(
                320,
                320,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.label.setPixmap(pixmap)

        except Exception as e:
            QMessageBox.critical(
                None,
                "Lỗi",
                str(e)
            )


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()

    # test id điểm danh
    ui = DD_ViewImage("DD001")

    ui.setupUi(Form)

    Form.show()

    sys.exit(app.exec())