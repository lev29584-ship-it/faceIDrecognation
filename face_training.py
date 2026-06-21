import cv2
import numpy as np
from PIL import Image
import os
from PyQt6.QtCore import QThread, pyqtSignal

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class face_training(QThread):
    # Tạo tín hiệu để báo cáo kết quả về giao diện khi train xong
    finished = pyqtSignal(bool, str)

    def __init__(self):
        super().__init__()
        self.path = os.path.join(BASE_DIR, 'image', 'photo')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        
        cascade_path = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")
        self.detector = cv2.CascadeClassifier(cascade_path)

        if self.detector.empty():
            print("Lỗi: Không load được Haar Cascade!")

    def getImagesAndLabels(self, path):
        faceSamples = []
        ids = []
        if not os.path.exists(path):
            return faceSamples, ids

        imagePaths = [
            os.path.join(path, f) for f in os.listdir(path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]

        for imagePath in imagePaths:
            try:
                PIL_img = Image.open(imagePath).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')
                
                filename = os.path.basename(imagePath)
                # Tách mã sinh viên (Ví dụ: SV001-image1.jpg -> lấy phần số 001)
                id_str = filename.split('-')[0].replace('SV', '') 
                
                if id_str.isdigit():
                    id_num = int(id_str)
                else:
                    continue

                faces = self.detector.detectMultiScale(img_numpy, scaleFactor=1.2, minNeighbors=5)
                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y+h, x:x+w])
                    ids.append(id_num)
            except Exception as e:
                print(f"Lỗi file {imagePath}: {e}")

        return faceSamples, ids

    # Hàm run() sẽ tự động chạy ngầm khi gọi .start()
    def run(self):
        try:
            faces, ids = self.getImagesAndLabels(self.path)

            if len(faces) == 0:
                self.finished.emit(False, "Không tìm thấy dữ liệu ảnh để training!")
                return

            self.recognizer.train(faces, np.array(ids))

            save_dir = "TrainingImageLabel"
            os.makedirs(save_dir, exist_ok=True)
            model_path = os.path.join(save_dir, "Trainner.yml")
            self.recognizer.write(model_path)

            self.finished.emit(True, f"Training thành công {len(set(ids))} sinh viên với {len(faces)} ảnh!")
        except Exception as e:
            self.finished.emit(False, f"Lỗi trong quá trình train: {str(e)}")

            