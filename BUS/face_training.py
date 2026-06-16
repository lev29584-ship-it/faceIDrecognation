from PyQt6.QtWidgets import QMessageBox, QWidget
import cv2
import numpy as np
from PIL import Image
import os
import re


class face_training(QWidget):
    def __init__(self):
        super().__init__()

        self.path = r'image\photo'

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        cascade_path = "haarcascade_frontalface_default.xml"
        self.detector = cv2.CascadeClassifier(cascade_path)

        if self.detector.empty():
            raise Exception("Không load được Haar Cascade!")

    # ======================
    # 📥 LOAD DATASET
    # ======================
    def getImagesAndLabels(self, path):
        faceSamples = []
        ids = []

        if not os.path.exists(path):
            raise Exception(f"Folder không tồn tại: {path}")

        imagePaths = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]

        for imagePath in imagePaths:
            try:
                PIL_img = Image.open(imagePath).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')

                filename = os.path.basename(imagePath)

                # ======================
                # 🔧 SAFE PARSE ID
                # ======================
                match = re.findall(r"\d+", filename)
                if not match:
                    continue

                id_num = int(match[0])

                faces = self.detector.detectMultiScale(
                    img_numpy,
                    scaleFactor=1.2,
                    minNeighbors=5
                )

                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y+h, x:x+w])
                    ids.append(id_num)

            except Exception as e:
                print(f"Lỗi file {imagePath}: {e}")

        return faceSamples, ids

    # ======================
    # 🧠 TRAIN MODEL
    # ======================
    def train(self):
        QMessageBox.information(
            self,
            "Thông báo",
            "Đang training... Vui lòng chờ"
        )

        faces, ids = self.getImagesAndLabels(self.path)

        if len(faces) == 0:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu khuôn mặt!")
            return

        try:
            self.recognizer.train(faces, np.array(ids))
        except Exception as e:
            QMessageBox.critical(self, "Lỗi Train", str(e))
            return

        # ======================
        # 💾 SAVE MODEL
        # ======================
        save_dir = "TrainingImageLabel"
        os.makedirs(save_dir, exist_ok=True)

        model_path = os.path.join(save_dir, "Trainer.yml")
        self.recognizer.write(model_path)

        QMessageBox.information(
            self,
            "Thành công",
            f"Training xong!\nSố mẫu: {len(faces)}"
        )