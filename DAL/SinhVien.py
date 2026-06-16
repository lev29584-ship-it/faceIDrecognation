class SinhVien:
    def __init__(self, masinhvien, hoten, malop, cmnd, gioitinh, ngsinh, email, sodienthoai, khoahoc):
        self._masinhvien = masinhvien
        self._hoten = hoten
        self._malop = malop
        self._cmnd = cmnd
        self._gioitinh = gioitinh
        self._ngsinh = ngsinh
        self._email = email
        self._sodienthoai = sodienthoai
        self._khoahoc = khoahoc

    # ===== GET =====
    def getMaSinhVien(self):
        return self._masinhvien

    def getHoTen(self):
        return self._hoten

    def getMaLop(self):
        return self._malop

    def getCMND(self):
        return self._cmnd

    def getGioiTinh(self):
        return self._gioitinh

    def getNgaySinh(self):
        return self._ngsinh

    def getEmail(self):
        return self._email

    def getSoDienThoai(self):
        return self._sodienthoai

    def getKhoaHoc(self):
        return self._khoahoc

    # ===== SET =====
    def setMaSinhVien(self, masinhvien):
        self._masinhvien = masinhvien

    def setHoTen(self, hoten):
        self._hoten = hoten

    def setMaLop(self, malop):
        self._malop = malop

    def setCMND(self, cmnd):
        self._cmnd = cmnd

    def setGioiTinh(self, gioitinh):
        self._gioitinh = gioitinh

    def setNgaySinh(self, ngsinh):
        self._ngsinh = ngsinh

    def setEmail(self, email):
        self._email = email

    def setSoDienThoai(self, sodienthoai):
        self._sodienthoai = sodienthoai

    def setKhoaHoc(self, khoahoc):
        self._khoahoc = khoahoc