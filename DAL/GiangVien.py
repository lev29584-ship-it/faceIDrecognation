class GiangVien:

    def __init__(
        self,
        magiangvien=None,
        hoten=None,
        sodienthoai=None,
        mataikhoan=None
    ):
        self.magiangvien = magiangvien
        self.hoten = hoten
        self.sodienthoai = sodienthoai
        self.mataikhoan = mataikhoan

    # ======================
    # 🧠 DEBUG
    # ======================
    def __repr__(self):
        return f"<GiangVien {self.magiangvien} - {self.hoten}>"

    # ======================
    # 🔍 VALIDATE BASIC
    # ======================
    def is_valid(self):
        return all([
            self.magiangvien,
            self.hoten,
            self.sodienthoai
        ])