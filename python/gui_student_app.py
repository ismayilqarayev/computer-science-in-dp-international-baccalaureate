import tkinter as tk
from tkinter import ttk

from student_models import GraduateStudent, PhDStudent, build_student_info
from student_validator import StudentValidator


class StudentApp:
    """GUI tətbiqinin əsas sinifi."""

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


def run_gui_mode():
    root = tk.Tk()
    StudentApp(root)
    root.mainloop()
