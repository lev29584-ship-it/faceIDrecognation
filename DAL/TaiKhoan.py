class TaiKhoan:
    def __init__(self, mataikhoan, email, matkhau, maquyen):
        self._mataikhoan = mataikhoan
        self._email = email
        self._matkhau = matkhau
        self._maquyen = maquyen

    # ===== GET =====
    def getMaTaiKhoan(self):
        return self._mataikhoan

    def getEmail(self):
        return self._email

    def getMatKhau(self):
        return self._matkhau

    def getMaQuyen(self):
        return self._maquyen

    # ===== SET =====
    def setMaTaiKhoan(self, mataikhoan):
        self._mataikhoan = mataikhoan

    def setEmail(self, email):
        self._email = email

    def setMatKhau(self, matkhau):
        self._matkhau = matkhau

    def setMaQuyen(self, maquyen):
        self._maquyen = maquyen