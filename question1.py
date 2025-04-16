class StudentDatabase:
    # Class attribute (list of all Student objects)
    student_list = []

    @classmethod
    def add_student(cls, student_obj):
        """
        Add a student object to the student_list.
        """
        cls.student_list.append(student_obj)
