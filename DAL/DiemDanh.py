class DiemDanh:

    def __init__(
        self,
        madiemdanh=None,
        masinhvien=None,
        giovao=None,
        giora=None,
        mabuoihoc=None,
        hinhanh=None
    ):
        self.madiemdanh = madiemdanh
        self.masinhvien = masinhvien
        self.giovao = giovao
        self.giora = giora
        self.mabuoihoc = mabuoihoc
        self.hinhanh = hinhanh

    # ======================
    # 🧠 DEBUG
    # ======================
    def __repr__(self):
        return f"<DiemDanh {self.madiemdanh} - {self.masinhvien} - {self.mabuoihoc}>"

    # ======================
    # 🔍 VALIDATE BASIC
    # ======================
    def is_valid(self):
        return all([
            self.masinhvien,
            self.mabuoihoc,
            self.giovao
        ])