import tkinter as tk
from tkinter import messagebox, ttk

from student_core import Student, StudentRepository, StudentValidator


class StudentForm(ttk.LabelFrame):
    def __init__(self, parent, on_add, on_update, on_delete, on_clear):
        super().__init__(parent, text="Student details", padding=14)

        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()

        self.create_fields()
        self.create_buttons(on_add, on_update, on_delete, on_clear)

    def create_fields(self):
        fields = (
            ("Ad", self.first_name_var),
            ("Soyad", self.last_name_var),
            ("Email", self.email_var),
            ("Telefon", self.phone_var),
        )

        for row, (label, variable) in enumerate(fields):
            ttk.Label(self, text=label).grid(row=row, column=0, sticky=tk.W, pady=6)
            ttk.Entry(self, textvariable=variable, width=30).grid(
                row=row,
                column=1,
                sticky="ew",
                pady=6,
                padx=(10, 0),
            )

    def create_buttons(self, on_add, on_update, on_delete, on_clear):
        button_frame = ttk.Frame(self)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(16, 0), sticky="ew")
        button_frame.columnconfigure((0, 1), weight=1)

        ttk.Button(button_frame, text="Elave et", command=on_add).grid(
            row=0, column=0, sticky="ew", padx=(0, 6)
        )
        ttk.Button(button_frame, text="Redakte et", command=on_update).grid(
            row=0, column=1, sticky="ew", padx=(6, 0)
        )
        ttk.Button(button_frame, text="Sil", command=on_delete).grid(
            row=1, column=0, sticky="ew", padx=(0, 6), pady=(10, 0)
        )
        ttk.Button(button_frame, text="Temizle", command=on_clear).grid(
            row=1, column=1, sticky="ew", padx=(6, 0), pady=(10, 0)
        )

    def get_student(self, student_id=None):
        return Student(
            first_name=self.first_name_var.get().strip(),
            last_name=self.last_name_var.get().strip(),
            email=self.email_var.get().strip(),
            phone=self.phone_var.get().strip(),
            student_id=student_id,
        )

    def set_student(self, student):
        self.first_name_var.set(student.first_name)
        self.last_name_var.set(student.last_name)
        self.email_var.set(student.email)
        self.phone_var.set(student.phone)

    def clear(self):
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")


class StudentTable(ttk.Frame):
    COLUMNS = ("id", "first_name", "last_name", "email", "phone")

    def __init__(self, parent, on_select):
        super().__init__(parent)
        self.tree = ttk.Treeview(
            self,
            columns=self.COLUMNS,
            show="headings",
            selectmode="browse",
        )

        self.create_columns()
        self.create_scrollbar()
        self.tree.bind("<<TreeviewSelect>>", on_select)

    def create_columns(self):
        headings = {
            "id": "ID",
            "first_name": "Ad",
            "last_name": "Soyad",
            "email": "Email",
            "phone": "Telefon",
        }
        widths = {
            "id": 55,
            "first_name": 130,
            "last_name": 130,
            "email": 220,
            "phone": 130,
        }

        for column in self.COLUMNS:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column])

        self.tree.column("id", anchor=tk.CENTER)

    def create_scrollbar(self):
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_students(self, students):
        self.clear()
        for student in students:
            self.tree.insert("", tk.END, values=student.to_table_values())

    def get_selected_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            return None

        values = self.tree.item(selected_item, "values")
        if not values:
            return None

        return Student.from_row(values)

    def clear_selection(self):
        self.tree.selection_remove(self.tree.selection())

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.repository = StudentRepository()
        self.selected_student_id = None

        self.configure_window()
        self.create_widgets()
        self.refresh_students()

    def configure_window(self):
        self.root.title("Student Management")
        self.root.geometry("850x520")
        self.root.minsize(760, 460)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def create_widgets(self):
        title = ttk.Label(
            self.root,
            text="Student Management",
            font=("Segoe UI", 20, "bold"),
        )
        title.pack(pady=(16, 10))

        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.form = StudentForm(
            main_frame,
            on_add=self.add_student,
            on_update=self.update_student,
            on_delete=self.delete_student,
            on_clear=self.clear_form,
        )
        self.form.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 14))

        self.table = StudentTable(main_frame, on_select=self.select_student)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def add_student(self):
        student = self.form.get_student()
        if not self.is_valid(student):
            return

        self.repository.add(student)
        self.after_change("Telebe elave edildi.")

    def update_student(self):
        if self.selected_student_id is None:
            messagebox.showwarning("Warning", "Redakte etmek ucun telebe secin.")
            return

        student = self.form.get_student(self.selected_student_id)
        if not self.is_valid(student):
            return

        self.repository.update(student)
        self.after_change("Telebe melumatlari yenilendi.")

    def delete_student(self):
        if self.selected_student_id is None:
            messagebox.showwarning("Warning", "Silmek ucun telebe secin.")
            return

        confirmed = messagebox.askyesno(
            "Confirm delete",
            "Secilmis telebeni silmek isteyirsiniz?",
        )
        if not confirmed:
            return

        self.repository.delete(self.selected_student_id)
        self.after_change("Telebe silindi.")

    def select_student(self, _event):
        student = self.table.get_selected_student()
        if student is None:
            return

        self.selected_student_id = student.student_id
        self.form.set_student(student)

    def refresh_students(self):
        self.table.load_students(self.repository.get_all())

    def clear_form(self):
        self.selected_student_id = None
        self.form.clear()
        self.table.clear_selection()

    def after_change(self, message):
        self.refresh_students()
        self.clear_form()
        messagebox.showinfo("Success", message)

    def is_valid(self, student):
        is_valid, error_message = StudentValidator.validate(student)
        if not is_valid:
            messagebox.showwarning("Warning", error_message)
        return is_valid

    def close(self):
        self.repository.close()
        self.root.destroy()


def run_app():
    root = tk.Tk()
    ttk.Style(root).theme_use("clam")
    StudentManagementApp(root)
    root.mainloop()
