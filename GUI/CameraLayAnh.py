from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

import cv2
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from BUS.face_dataset import face_dataset


class CameraLayAnh(object):

    def __init__(self, idSV):
        self.idSV = idSV
        self.thread = None
        self.is_running = False

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # ===== CAMERA LABEL =====
        self.label = QtWidgets.QLabel("Camera")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("border: 1px solid black;")

        self.layout.addWidget(self.label)

        # ===== BUTTON =====
        self.btn_capture = QtWidgets.QPushButton("Chụp ảnh")
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_capture.setFont(font)

        self.btn_capture.clicked.connect(self.start_capture_video)

        self.layout.addWidget(self.btn_capture)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lấy ảnh sinh viên"))

    # =========================
    # START CAMERA
    # =========================
    def start_capture_video(self):

        if self.is_running:
            QMessageBox.warning(
                self.centralwidget,
                "Thông báo",
                "Camera đang chạy"
            )
            return

        self.is_running = True

        try:
            self.thread = face_dataset(1, self.idSV)

            self.thread.signal.connect(self.show_webcam)
            self.thread.finished.connect(self.thread_finished)

            self.thread.start()

        except Exception as e:
            self.is_running = False
            QMessageBox.critical(self.centralwidget, "Lỗi", str(e))

    # =========================
    # SHOW FRAME
    # =========================
    def show_webcam(self, cv_img):

        # camera stop signal
        if isinstance(cv_img, (list, tuple)) and len(cv_img) == 1 and cv_img[0] == 0:
            QMessageBox.information(
                self.centralwidget,
                "Thông báo",
                "Lấy ảnh sinh viên thành công."
            )
            self.is_running = False
            return

        if cv_img is None:
            return

        try:
            pixmap = self.convert_cv_qt(cv_img)
            self.label.setPixmap(pixmap)
        except Exception as e:
            print("Lỗi hiển thị webcam:", e)

    # =========================
    # CONVERT OPENCV -> QT
    # =========================
    def convert_cv_qt(self, cv_img):

        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        qt_image = QtGui.QImage(
            rgb_image.data,
            w,
            h,
            bytes_per_line,
            QtGui.QImage.Format.Format_RGB888
        )

        scaled = qt_image.scaled(
            640,
            480,
            Qt.AspectRatioMode.KeepAspectRatio
        )

        return QtGui.QPixmap.fromImage(scaled)

    # =========================
    # THREAD FINISHED
    # =========================
    def thread_finished(self):
        self.is_running = False
        self.thread = None


# =========================
# RUN TEST
# =========================
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = CameraLayAnh("SV001")
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())