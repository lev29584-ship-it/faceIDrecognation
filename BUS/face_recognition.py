import cv2
import numpy as np
import time
from PyQt6.QtCore import QThread, pyqtSignal
from .SinhVienBUS import SinhVienBUS


class face_recognition(QThread):
    signal = pyqtSignal(np.ndarray)

    def __init__(self, index, permission=None):
        super(face_recognition, self).__init__()

        self.index = index
        self.permission = permission

        self.running = False
        self.cap = None

        self.masinhvien_save = None
        self.cv_img_cur = None
        self.link_image = None

        # 🔥 cache BUS (QUAN TRỌNG)
        self.sv_bus = SinhVienBUS()

        # tránh gọi DB liên tục
        self.user_cache = {}

    # ======================
    # 🔐 CHECK PERMISSION
    # ======================
    def check_permission(self):
        if not self.permission:
            return False

        permissions = getattr(self.permission, "permissions", [])
        return "CN_FACE_RECOGNITION" in permissions

    # ======================
    # 🛑 STOP THREAD
    # ======================
    def stop(self):
        self.running = False

    # ======================
    # 🚀 MAIN RUN
    # ======================
    def run(self):

        if not self.check_permission():
            print("❌ Không có quyền Face Recognition")
            return

        self.running = True

        cap = cv2.VideoCapture(self.index, cv2.CAP_DSHOW)
        self.cap = cap

        if not cap.isOpened():
            print("❌ Cannot open camera")
            return

        # ======================
        # AI MODEL
        # ======================
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("TrainingImageLabel/Trainner.yml")

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml"
        )

        font = cv2.FONT_HERSHEY_SIMPLEX

        minW = 0.1 * cap.get(3)
        minH = 0.1 * cap.get(4)

        while self.running:
            try:
                ret, frame = cap.read()
                if not ret or frame is None:
                    self.msleep(10)
                    continue

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int(minW), int(minH)),
                )

                for (x, y, w, h) in faces:

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    id_pred, conf = recognizer.predict(gray[y:y+h, x:x+w])

                    masv = f"SV{id_pred:03}"

                    # ======================
                    # CACHE USER (GIẢM BUS CALL)
                    # ======================
                    if masv not in self.user_cache:
                        users = self.sv_bus.findMaSinhVien(masv)
                        ten = ""

                        if users:
                            for row in users:
                                ten = row[1]

                        self.user_cache[masv] = ten

                    ten = self.user_cache.get(masv, "")

                    # ======================
                    # CONFIDENCE LOGIC
                    # ======================
                    if conf < 55:
                        label = f"{masv}-{ten}"
                        confidence_text = f"{round(100 - conf)}%"

                        # lưu 1 lần
                        if conf < 45 and masv != self.masinhvien_save:
                            self.masinhvien_save = masv
                            self.cv_img_cur = gray[y:y+h, x:x+w]

                            t = time.localtime()
                            current_time = time.strftime("%H_%M_%S", t)

                            self.link_image = f"./image/diemdanh/{masv}_{current_time}.jpg"
                            cv2.imwrite(self.link_image, self.cv_img_cur)

                    else:
                        label = "Unknown"
                        confidence_text = f"{round(100 - conf)}%"

                    cv2.putText(
                        frame,
                        label,
                        (x + 5, y - 5),
                        font,
                        1,
                        (255, 255, 255),
                        2
                    )

                self.signal.emit(frame)

            except Exception as ex:
                print("Camera loop error:", ex)
                self.msleep(50)

        # ======================
        # CLEANUP
        # ======================
        if self.cap:
            self.cap.release()
            self.cap = None

        cv2.destroyAllWindows()

    # ======================
    # GETTERS
    # ======================
    def getIDSV(self):
        return self.masinhvien_save

    def getCv_Image_Cur(self):
        return self.cv_img_cur

    def getLink_Image(self):
        return self.link_image