class HinhAnhSV:

    def __init__(
        self,
        mahinhanh=None,
        masinhvien=None,
        duongdan=None,
        thoigian=None
    ):
        self.mahinhanh = mahinhanh
        self.masinhvien = masinhvien
        self.duongdan = duongdan
        self.thoigian = thoigian

    # ======================
    # DEBUG
    # ======================
    def __repr__(self):
        return f"<HinhAnhSV {self.masinhvien} - {self.duongdan}>"

    # ======================
    # VALIDATE
    # ======================
    def is_valid(self):
        return all([
            self.masinhvien,
            self.duongdan
        ])