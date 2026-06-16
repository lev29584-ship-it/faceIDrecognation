class BuoiHoc:
    def __init__(
        self,
        mabuoihoc=None,
        giobatdau=None,
        gioketthuc=None,
        ngay=None,
        malop=None,
        magiangvien=None
    ):
        self.mabuoihoc = mabuoihoc
        self.giobatdau = giobatdau
        self.gioketthuc = gioketthuc
        self.ngay = ngay
        self.malop = malop
        self.magiangvien = magiangvien

    # ======================
    # 🧠 DEBUG STRING
    # ======================
    def __repr__(self):
        return f"<BuoiHoc {self.mabuoihoc} - {self.malop} - {self.ngay}>"

    # ======================
    # 🔍 VALIDATE BASIC
    # ======================
    def is_valid(self):
        return all([
            self.mabuoihoc,
            self.giobatdau,
            self.gioketthuc,
            self.ngay,
            self.malop,
            self.magiangvien
        ])