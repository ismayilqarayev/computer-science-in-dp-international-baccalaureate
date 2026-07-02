from student_models import GraduateStudent, PhDStudent
from student_validator import StudentValidator


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
