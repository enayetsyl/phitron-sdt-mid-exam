from question1 import StudentDatabase

class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        # Private attributes
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        # Insert this student into the StudentDatabase
        StudentDatabase.add_student(self)

    def enroll_student(self):
        """
        Enroll the student if not already enrolled.
        Raise an exception if the student is already enrolled.
        """
        if self.__is_enrolled:
            raise ValueError(f"Student {self.__student_id} is already enrolled.")
        self.__is_enrolled = True

    def drop_student(self):
        """
        Drop the student (change is_enrolled to False).
        Raise an exception if the student is not enrolled.
        """
        if not self.__is_enrolled:
            raise ValueError(f"Student {self.__student_id} is not currently enrolled.")
        self.__is_enrolled = False

    def view_student_info(self):
        """
        Display student details.
        """
        enrollment_status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id}, Name: {self.__name}, "
              f"Department: {self.__department}, Status: {enrollment_status}")

    # Optionally, you might want to provide read-only properties to safely access
    # the private attributes if needed elsewhere, for example:
    @property
    def student_id(self):
        return self.__student_id

    @property
    def is_enrolled(self):
        return self.__is_enrolled