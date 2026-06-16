import re


class CheckError:

    # =========================
    # PHONE
    # =========================
    @staticmethod
    def check_phone(phone):
        phone = str(phone).strip()

        pattern = r"^(0|\+84)(\s|\.)?((3[2-9])|(5[689])|(7[06-9])|(8[1-689])|(9[0-46-9]))(\d)(\s|\.)?(\d{3})(\s|\.)?(\d{3})$"

        return bool(re.match(pattern, phone))

    # =========================
    # EMAIL
    # =========================
    @staticmethod
    def check_email(email):
        email = str(email).strip()

        pattern = r"^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@" \
                  r"[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$"

        return bool(re.match(pattern, email))

    # =========================
    # CMND / CCCD
    # =========================
    @staticmethod
    def check_cmnd(cmnd):
        cmnd = str(cmnd).strip()

        pattern = r"^[0-9]{9}$|^[0-9]{12}$"

        return bool(re.match(pattern, cmnd))

    # =========================
    # MSSV (NÊN DÙNG CHO GUI)
    # =========================
    @staticmethod
    def check_mssv(mssv):
        mssv = str(mssv).strip()

        # ví dụ: SV001, SV2024001...
        pattern = r"^[A-Z]{2,3}[0-9]{2,10}$"

        return bool(re.match(pattern, mssv))

    # =========================
    # VALIDATE ALL (DÙNG TRONG GUI)
    # =========================
    @staticmethod
    def validate_student(data: dict):

        errors = []

        if not data.get("masv"):
            errors.append("Mã sinh viên không được rỗng")
        elif not CheckError.check_mssv(data["masv"]):
            errors.append("Mã sinh viên không hợp lệ")

        if not data.get("email"):
            errors.append("Email không được rỗng")
        elif not CheckError.check_email(data["email"]):
            errors.append("Email không hợp lệ")

        if data.get("sdt") and not CheckError.check_phone(data["sdt"]):
            errors.append("Số điện thoại không hợp lệ")

        if data.get("cmnd") and not CheckError.check_cmnd(data["cmnd"]):
            errors.append("CMND/CCCD không hợp lệ")

        return errors