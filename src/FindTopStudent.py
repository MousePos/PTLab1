from CalcRating import RatingType
from Types import DataType
from YMLDataReader import YamlDataReader
import yaml

class StudentFinder:

    def __init__(self, data_reader: YamlDataReader, file_path: str):
        self.students = self.load_and_filter_students(data_reader, file_path)

    def load_and_filter_students(self, data_reader: YamlDataReader, file_path: str) -> list[str]:
        data = data_reader.read(file_path)
        
        students_above_90 = []

        for student_data in data:
            for name, grades in student_data.items():
                if all(grade >= 90 for grade in grades.values()):
                    students_above_90.append(name)
        return students_above_90

    def print_students_above_90(self):
        if not self.students:
            print("Нет студентов с оценками выше 90.")
        for student in self.students:
            print(student)