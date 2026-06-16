class ChucNang:
    def __init__(self, machucnang=None, tenchucnang=None):
        self.machucnang = machucnang
        self.tenchucnang = tenchucnang

    def __repr__(self):
        return f"<ChucNang {self.machucnang} - {self.tenchucnang}>"

    def is_valid(self):
        return bool(self.machucnang and self.tenchucnang)