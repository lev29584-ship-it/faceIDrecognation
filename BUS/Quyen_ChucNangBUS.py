from DAL.Quyen_ChucNangDAL import Quyen_ChucNangDAL
from DAL.Quyen_ChucNang import Quyen_ChucNang


class Quyen_ChucNangBUS:
    def __init__(self, permission=None):
        self.permission = permission

    # ======================
    # 🔐 CHECK PERMISSION
    # ======================
    def _check_permission(self, roles):
        if not self.permission:
            raise Exception("Chưa đăng nhập")

        if self.permission.role not in roles:
            raise Exception("Không có quyền thực hiện chức năng này")

    # ======================
    # 📥 GET
    # ======================
    def get(self):
        return Quyen_ChucNangDAL.get()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return Quyen_ChucNangDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, q: Quyen_ChucNang):
        self._check_permission(["ADMIN"])

        if not q:
            raise Exception("Dữ liệu không hợp lệ")

        if self.checkExists(q.maquyen, q.machucnang):
            raise Exception("Quyền đã có chức năng này")

        return Quyen_ChucNangDAL.add(q)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, q: Quyen_ChucNang):
        self._check_permission(["ADMIN"])

        if not q:
            raise Exception("Dữ liệu không hợp lệ")

        return Quyen_ChucNangDAL.update(q)

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id: int):
        self._check_permission(["ADMIN"])

        if not id:
            raise Exception("ID không hợp lệ")

        return Quyen_ChucNangDAL.delete(id)

    # ======================
    # 📥 GET BY ROLE
    # ======================
    def getListChucNangTheoQuyen(self, maquyen):
        return Quyen_ChucNangDAL.getListChucNangTheoQuyen(maquyen)

    # ======================
    # 🔍 CHECK EXISTS (FIX LOGIC)
    # ======================
    def checkExists(self, maquyen, machucnang):
        data = Quyen_ChucNangDAL.getListChucNangTheoQuyen(maquyen)

        if not data:
            return False

        # normalize dữ liệu để tránh sai kiểu
        return any(str(x) == str(machucnang) for x in data)