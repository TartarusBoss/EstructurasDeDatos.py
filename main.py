class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grade = grades

    def add_grade(self, grade):
        self.grades.append(grade)
        return
    def average_grade(self, grades):
        sum(self.grades) / len(self.grades)
        return
    def diccionarios(self):

        lista = [
            {"name": "Matias", "age": 18, "grades": [4, 7, 3, 5, 6]},
            {"name": "Maria", "age": 18, "grades": [2, 1, 3, 4, 6]},
            {"name": "Mateo", "age": 20, "grades": [7, 2, 1, 4, 3]},
            {"name": "Santiago", "age": 16, "grades": [1, 2, 5, 7, 2]},
            {"name": "Ana", "age": 15, "grades": [2, 1, 5, 8, 9]}
        ]

        comprehension = [

            Student(estudiante["name"], estudiante["age"], estudiante["grades"])
            for estudiante in lista

        ]

        promedio = 6

        filtro_aplicado = [
            Student(estudiante["name"], estudiante["age"], estudiante["grades"])
            for estudiante in lista
            if sum(estudiante["grades"]) / len(estudiante["grades"]) >= promedio
        ]

        return filtro_aplicado



