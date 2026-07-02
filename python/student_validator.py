import re
from tkinter import messagebox


class StudentValidator:
    """Məlumatların doğrulanması üçün OOP əsaslı köməkçi sinif."""

    def validate(self, data):
        if any(not value for value in data.values()):
            messagebox.showerror("Error", "All fields are required")
            return False
        if not self.is_valid_phone(data["Phone"]):
            messagebox.showerror("Error", "Invalid phone number")
            return False
        if not self.is_valid_email(data["Email"]):
            messagebox.showerror("Error", "Invalid email format")
            return False
        return True

    def is_valid_phone(self, phone):
        return bool(re.fullmatch(r"\+?[0-9\-\s]{7,20}", phone))

    def is_valid_email(self, email):
        return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email))
