class Quyen_ChucNang:
    def __init__(self, maquyen, machucnang):
        self._maquyen = maquyen
        self._machucnang = machucnang

    # ===== GET =====
    def getMaQuyen(self):
        return self._maquyen

    def getMaChucNang(self):
        return self._machucnang

    # ===== SET =====
    def setMaQuyen(self, maquyen):
        self._maquyen = maquyen

    def setMaChucNang(self, machucnang):
        self._machucnang = machucnang

    # ===== DEBUG =====
    def __repr__(self):
        return f"Quyen_ChucNang(maquyen={self._maquyen}, machucnang={self._machucnang})"