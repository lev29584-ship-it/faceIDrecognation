from DAL.TaiKhoanDAL import TaiKhoanDAL
from DAL.TaiKhoan import TaiKhoan


class TaiKhoanBUS:
    def __init__(self):
        self.dal = TaiKhoanDAL()
        self._cache_login = None

    # ======================
    # 📥 GET
    # ======================
    def get(self):
        return self.dal.get()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return self.dal.generateID()

    # ======================
    # ➕ ADD ACCOUNT
    # ======================
    def add(self, tk: TaiKhoan):
        if not tk:
            raise Exception("Dữ liệu tài khoản không hợp lệ")

        if self.checkEmailTonTai(tk.email):
            raise Exception("Email đã tồn tại")

        return self.dal.add(tk)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, tk: TaiKhoan):
        if not tk:
            raise Exception("Dữ liệu tài khoản không hợp lệ")

        return self.dal.update(tk)

    # ======================
    # ❌ DELETE (CHẶN ADMIN)
    # ======================
    def delete(self, id: int):
        if not id:
            raise Exception("ID không hợp lệ")

        if self.checkNotTaiKhoanAdmin(id):
            raise Exception("Không thể xóa tài khoản Admin")

        return self.dal.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return self.dal.find(key, value)

    # ======================
    # 🔐 LOGIN
    # ======================
    def checkLogin(self, email, password):
        if not email or not password:
            return None

        user = self.dal.checkLogin(email, password)

        self._cache_login = user
        return user

    # ======================
    # 🔑 CHANGE PASSWORD
    # ======================
    def changePassword(self, email, mkmoi):
        if not email or not mkmoi:
            raise Exception("Dữ liệu không hợp lệ")

        return self.dal.changePassword(email, mkmoi)

    # ======================
    # 🛑 CHECK ADMIN ACCOUNT
    # ======================
    def checkNotTaiKhoanAdmin(self, mataikhoan):
        return self.dal.checkNotTaiKhoanAdmin(mataikhoan)

    # ======================
    # 📧 CHECK EMAIL EXISTS
    # ======================
    def checkEmailTonTai(self, email):
        return self.dal.checkEmailTonTai(email)

    # ======================
    # 👤 CURRENT USER (RBAC CORE)
    # ======================
    def getCurrentUser(self):
        return self._cache_login