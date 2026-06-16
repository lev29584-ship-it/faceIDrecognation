from DAL.QuyenDAL import QuyenDAL
from DAL.Quyen import Quyen


class QuyenBUS:
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
        return QuyenDAL.get()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return QuyenDAL.generateID()

    # ======================
    # ➕ ADD ROLE
    # ======================
    def add(self, q: Quyen):
        self._check_permission(["ADMIN"])

        if not q:
            raise Exception("Dữ liệu không hợp lệ")

        if not getattr(q, "tenquyen", None):
            raise Exception("Thiếu tên quyền")

        if self.checkTenQuyenTonTai(q.tenquyen):
            raise Exception("Tên quyền đã tồn tại")

        return QuyenDAL.add(q)

    # ======================
    # ✏️ UPDATE ROLE
    # ======================
    def update(self, q: Quyen):
        self._check_permission(["ADMIN"])

        if not q:
            raise Exception("Dữ liệu không hợp lệ")

        return QuyenDAL.update(q)

    # ======================
    # ❌ DELETE ROLE
    # ======================
    def delete(self, id: int):
        self._check_permission(["ADMIN"])

        if not id:
            raise Exception("ID không hợp lệ")

        return QuyenDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return QuyenDAL.find(key, value)

    # ======================
    # 🔍 CHECK EXIST ROLE
    # ======================
    def checkTenQuyenTonTai(self, tenquyen):
        if not tenquyen:
            return False

        return QuyenDAL.checkTenQuyenTonTai(tenquyen)

    # ======================
    # 👤 GET ROLE BY NAME
    # ======================
    def getRoleByName(self, tenquyen):
        if not tenquyen:
            return None

        result = QuyenDAL.find("tenquyen", tenquyen)

        # đảm bảo trả về 1 role duy nhất
        if isinstance(result, list):
            return result[0] if result else None

        return result