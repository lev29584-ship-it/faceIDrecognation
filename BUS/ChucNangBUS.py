class ChucNangBUS:
    def __init__(self):
        self._cache = None

    # ======================
    # 📥 GET (CACHE)
    # ======================
    def get(self):
        if self._cache is None:
            self._cache = ChucNangDAL.get()
        return self._cache

    # ======================
    # 🔄 REFRESH CACHE
    # ======================
    def refreshCache(self):
        self._cache = ChucNangDAL.get()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return ChucNangDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, cn: ChucNang):
        if not cn:
            raise Exception("Chức năng không hợp lệ")

        if not getattr(cn, "ten_chuc_nang", None):
            raise Exception("Thiếu tên chức năng")

        result = ChucNangDAL.add(cn)
        self.refreshCache()
        return result

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, cn: ChucNang):
        if not cn:
            raise Exception("Chức năng không hợp lệ")

        result = ChucNangDAL.update(cn)
        self.refreshCache()
        return result

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id):
        if not id:
            raise Exception("ID không hợp lệ")

        result = ChucNangDAL.delete(id)
        self.refreshCache()
        return result

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return ChucNangDAL.find(key, value)

    # ======================
    # 🔍 CHECK TÊN TỒN TẠI
    # ======================
    def checkTenCNTonTai(self, tenchucnang):
        return ChucNangDAL.checkTenCNTonTai(tenchucnang)

    # ======================
    # 🧠 MAP CHỨC NĂNG (RBAC CORE)
    # ======================
    def getMapChucNang(self):
        data = self.get()
        return {item[0]: item[1] for item in data}

    # ======================
    # 🔐 CHECK PERMISSION FEATURE
    # ======================
    def hasPermission(self, role_permissions, ma_chuc_nang):
        return ma_chuc_nang in role_permissions