class BuoiHocBUS:
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
    # 📥 GET (RBAC)
    # ======================
    def get(self):
        data = BuoiHocDAL.get()

        if not self.permission:
            return []

        role = self.permission.role

        if role == "ADMIN":
            return data

        if role == "MANAGER":
            class_id = getattr(self.permission, "class_id", None)
            return [
                x for x in data
                if getattr(x, "class_id", None) == class_id
            ]

        if role == "STUDENT":
            user_id = getattr(self.permission, "user_id", None)
            return [
                x for x in data
                if getattr(x, "user_id", None) == user_id
            ]

        return []

    # ======================
    # 📊 COUNT
    # ======================
    def countAll(self):
        # (giữ nguyên vì đây thường là admin tool)
        return BuoiHocDAL.countAll()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return BuoiHocDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, bh):
        self._check_permission(["ADMIN"])

        if not bh:
            raise Exception("Dữ liệu buổi học không hợp lệ")

        if not getattr(bh, "ma_buoi_hoc", None):
            raise Exception("Thiếu mã buổi học")

        return BuoiHocDAL.add(bh)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, bh):
        self._check_permission(["ADMIN", "MANAGER"])

        if not bh:
            raise Exception("Dữ liệu buổi học không hợp lệ")

        if not getattr(bh, "ma_buoi_hoc", None):
            raise Exception("Thiếu mã buổi học")

        return BuoiHocDAL.update(bh)

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id):
        self._check_permission(["ADMIN"])

        if not id:
            raise Exception("ID không hợp lệ")

        return BuoiHocDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return BuoiHocDAL.find(key, value)

    def findMaBuoiHoc(self, value):
        return BuoiHocDAL.findMaBuoiHoc(value)