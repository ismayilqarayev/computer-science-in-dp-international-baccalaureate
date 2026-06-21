from dataclasses import dataclass
from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("students.db")


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone: str
    student_id: int | None = None

    @classmethod
    def from_row(cls, row):
        student_id, first_name, last_name, email, phone = row
        return cls(first_name, last_name, email, phone, int(student_id))

    def to_db_values(self):
        return self.first_name, self.last_name, self.email, self.phone

    def to_table_values(self):
        return (
            self.student_id,
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
        )


class StudentRepository:
    def __init__(self, db_path=DB_PATH):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def add(self, student):
        self.connection.execute(
            """
            INSERT INTO students (first_name, last_name, email, phone)
            VALUES (?, ?, ?, ?)
            """,
            student.to_db_values(),
        )
        self.connection.commit()

    def update(self, student):
        self.connection.execute(
            """
            UPDATE students
            SET first_name = ?, last_name = ?, email = ?, phone = ?
            WHERE id = ?
            """,
            (*student.to_db_values(), student.student_id),
        )
        self.connection.commit()

    def delete(self, student_id):
        self.connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.connection.commit()

    def get_all(self):
        cursor = self.connection.execute(
            """
            SELECT id, first_name, last_name, email, phone
            FROM students
            ORDER BY id DESC
            """
        )
        return [Student.from_row(row) for row in cursor.fetchall()]

    def close(self):
        self.connection.close()


class StudentValidator:
    @staticmethod
    def validate(student):
        if not all(
            (student.first_name, student.last_name, student.email, student.phone)
        ):
            return False, "Butun xanalari doldurun."

        if "@" not in student.email or "." not in student.email:
            return False, "Duzgun email daxil edin."

        return True, ""
