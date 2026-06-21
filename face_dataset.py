import cv2
import numpy as np
import time
from PyQt6.QtCore import QThread, pyqtSignal

class face_dataset(QThread):
    signal = pyqtSignal(np.ndarray)

    def __init__(self, index, id, permission=None):
        super(face_dataset, self).__init__()

        self.index = index
        self.idSV = id
        self.permission = permission

        self._running = True
        self.cap = None

    # ======================
    # 🔐 CHECK PERMISSION (Đã sửa)
    # ======================
    def check_permission(self):
        # Trả về True luôn vì giao diện (main.py) đã lo việc phân quyền nút bấm
        if not self.permission:
            return True

        permissions = getattr(self.permission, "permissions", [])
        return "CN001" in permissions

    # ======================
    # 🛑 STOP THREAD
    # ======================
    def stop(self):
        self._running = False

    # ======================
    # 🚀 RUN THREAD
    # ======================
    def run(self):
        if not self.check_permission():
            print("❌ Không có quyền sử dụng Face Dataset")
            return

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("❌ Không mở được camera")
            return

        while self._running:
            ret, frame = self.cap.read()

            if not ret:
                time.sleep(0.01)
                continue

            self.signal.emit(frame)

            # 🔥 giảm CPU usage
            time.sleep(0.01)

        # ======================
        # 🧹 CLEAN UP
        # ======================
        if self.cap:
            self.cap.release()

        cv2.destroyAllWindows()