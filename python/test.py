from abc import ABC, abstractmethod
import re
import tkinter as tk
from tkinter import messagebox, ttk


# Ana tələbə sinifi: ümumi xüsusiyyətlər və abstract metod burada təyin olunur
class Student(ABC):
    def __init__(self, name, surname, phone_number, email):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @abstractmethod
    def show_info(self):
        pass


# Magistr/graduate tələbə üçün əlavə sahə: universitet
class GraduateStudent(Student):
    def __init__(self, name, surname, phone_number, email, university):
        super().__init__(name, surname, phone_number, email)
        self._university = university

    def show_info(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"Phone: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"University: {self._university}")


# PhD tələbə üçün əlavə sahə: tədqiqat mövzusu
class PhDStudent(GraduateStudent):
    def __init__(self, name, surname, phone_number, email, university, research_topic):
        super().__init__(name, surname, phone_number, email, university)
        self._research_topic = research_topic

    def show_info(self):
        super().show_info()
        print(f"Research Topic: {self._research_topic}")


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


class ConsoleStudentApp:
    """Konsol rejimi üçün OOP əsaslı tətbiq sinifi."""

    def __init__(self):
        self.validator = StudentValidator()

    def read_non_empty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Invalid entry: this field cannot be empty. Please enter a valid value.")

    def read_valid_phone(self, prompt):
        while True:
            phone = input(prompt).strip()
            if not phone:
                print("Invalid entry: phone number cannot be empty.")
                continue
            if self.validator.is_valid_phone(phone):
                return phone
            print("Invalid phone number. Use digits, spaces, dashes, and optional leading +.")

    def read_valid_email(self, prompt):
        while True:
            email = input(prompt).strip()
            if not email:
                print("Invalid entry: email cannot be empty.")
                continue
            if self.validator.is_valid_email(email):
                return email
            print("Invalid email format. Example: user@example.com")

    def run(self):
        print("Graduate student data entry:")
        gs_name = self.read_non_empty_input("Enter the name of the graduate student: ")
        gs_surname = self.read_non_empty_input("Enter the surname of the graduate student: ")
        gs_phone = self.read_valid_phone("Enter the phone number of the graduate student: ")
        gs_email = self.read_valid_email("Enter the email of the graduate student: ")
        gs_university = self.read_non_empty_input("Enter the university of the graduate student: ")

        graduate_student = GraduateStudent(gs_name, gs_surname, gs_phone, gs_email, gs_university)
        print()
        graduate_student.show_info()

        print()
        print("PhD student data entry:")
        phd_name = self.read_non_empty_input("Enter the name of the PhD student: ")
        phd_surname = self.read_non_empty_input("Enter the surname of the PhD student: ")
        phd_phone = self.read_valid_phone("Enter the phone number of the PhD student: ")
        phd_email = self.read_valid_email("Enter the email of the PhD student: ")
        phd_university = self.read_non_empty_input("Enter the university of the PhD student: ")
        phd_research_topic = self.read_non_empty_input("Enter the research topic of the PhD student: ")

        phd_student = PhDStudent(phd_name, phd_surname, phd_phone, phd_email, phd_university, phd_research_topic)
        print()
        phd_student.show_info()


def run_console_mode():
    ConsoleStudentApp().run()


# GUI tətbiqinin əsas sinifi
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.validator = StudentValidator()
        self.root.title("Student Information System")
        self.root.geometry("620x650")
        self.root.configure(bg="#0f172a")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=16, pady=16)

        self.create_graduate_tab()
        self.create_phd_tab()

    def create_graduate_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Graduate Student")

        fields = ["Name", "Surname", "Phone", "Email", "University"]
        self.grad_entries = {}

        for i, field in enumerate(fields):
            ttk.Label(frame, text=field).grid(row=i, column=0, sticky="w", padx=10, pady=(8, 2))
            entry = ttk.Entry(frame, width=40)
            entry.grid(row=i, column=1, padx=10, pady=(8, 2))
            self.grad_entries[field] = entry

        ttk.Button(frame, text="Show Graduate Student", command=self.add_graduate_student).grid(
            row=len(fields), column=0, columnspan=2, pady=16
        )

        self.grad_result = tk.Text(frame, height=12, width=48, wrap="word")
        self.grad_result.grid(row=len(fields) + 1, column=0, columnspan=2, padx=10, pady=8)

    def create_phd_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="PhD Student")

        fields = ["Name", "Surname", "Phone", "Email", "University", "Research Topic"]
        self.phd_entries = {}

        for i, field in enumerate(fields):
            ttk.Label(frame, text=field).grid(row=i, column=0, sticky="w", padx=10, pady=(8, 2))
            entry = ttk.Entry(frame, width=40)
            entry.grid(row=i, column=1, padx=10, pady=(8, 2))
            self.phd_entries[field] = entry

        ttk.Button(frame, text="Show PhD Student", command=self.add_phd_student).grid(
            row=len(fields), column=0, columnspan=2, pady=16
        )

        self.phd_result = tk.Text(frame, height=12, width=48, wrap="word")
        self.phd_result.grid(row=len(fields) + 1, column=0, columnspan=2, padx=10, pady=8)

    def add_graduate_student(self):
        data = self.get_values(self.grad_entries)
        if not self.validate(data):
            return

        student = GraduateStudent(data["Name"], data["Surname"], data["Phone"], data["Email"], data["University"])
        self.grad_result.delete("1.0", tk.END)
        self.grad_result.insert(tk.END, build_student_info(student))

    def add_phd_student(self):
        data = self.get_values(self.phd_entries)
        if not self.validate(data):
            return

        student = PhDStudent(
            data["Name"],
            data["Surname"],
            data["Phone"],
            data["Email"],
            data["University"],
            data["Research Topic"],
        )
        self.phd_result.delete("1.0", tk.END)
        self.phd_result.insert(tk.END, build_student_info(student))

    def get_values(self, entries):
        return {k: v.get().strip() for k, v in entries.items()}

    def validate(self, data):
        return self.validator.validate(data)


# GUI rejimini başlatmaq üçün funksiya
def run_gui_mode():
    root = tk.Tk()
    StudentApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui_mode()
