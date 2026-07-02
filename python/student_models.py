from abc import ABC, abstractmethod


class Student(ABC):
    """Ümumi tələbə davranışlarını təyin edən abstract baza sinfi."""

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


class GraduateStudent(Student):
    """Magistr/graduate tələbə üçün əlavə universitet sahəsi."""

    def __init__(self, name, surname, phone_number, email, university):
        super().__init__(name, surname, phone_number, email)
        self._university = university

    def show_info(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"Phone: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"University: {self._university}")


class PhDStudent(GraduateStudent):
    """PhD tələbə üçün tədqiqat mövzusu əlavə edilir."""

    def __init__(self, name, surname, phone_number, email, university, research_topic):
        super().__init__(name, surname, phone_number, email, university)
        self._research_topic = research_topic

    def show_info(self):
        super().show_info()
        print(f"Research Topic: {self._research_topic}")


def build_student_info(student):
    """Tələbə məlumatlarını göstərmək üçün mətn forması yaradır."""
    lines = [
        f"Name: {student.name} {student.surname}",
        f"Phone: {student.phone_number}",
        f"Email: {student.email}",
    ]

    if isinstance(student, GraduateStudent):
        lines.append(f"University: {student._university}")

    if isinstance(student, PhDStudent):
        lines.append(f"Research Topic: {student._research_topic}")

    return "\n".join(lines)
