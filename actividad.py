def Actividad_POO():
 class Student:
    def __init__(self, name, age, grades): #Metodo de constructor para inicializar c/u de los atributos
        self.name = name
        self.age = age
        self.grades = grades
    def add_grade(self, grade): #Metodo que recibe un numero cualqueira y lo añade a grades
        self.grades.append(grade)
    def average_grade(self): #Este metodo saca la nota promedio de grades, usando la función sum y len
        return sum(self.grades) / len(self.grades)
    def diccionarios(self): #Aca creamos la lista con los atributos que tenemos en (1)
        lista = [
            {"Nombre": "Matias", "Edad": 18, "grades": [4, 7, 3, 5, 6]},
            {"Nombre": "Maria", "Edad": 18, "grades": [2, 1, 3, 4, 6]},
            {"Nombre": "Mateo", "Edad": 20, "grades": [7, 2, 1, 4, 3]},
            {"Nombre": "Santiago", "Edad": 16, "grades": [1, 2, 5, 7, 2]},
            {"Nombre": "Ana", "Edad": 15, "grades": [2, 1, 5, 8, 9]}
        ]

        lista_comprehesion = [  #Acá creamos la lista_comprehesion que utiliza los objetos de la clase, usando la lista de diccionarios anterior
            Student(estudiante["name"], estudiante["age"], estudiante["grades"])
            for estudiante in lista
        ]

        promedio = 6 #Acá hacemos que el promedio sea una constante, podría ser cualquier numero

        filtrado = [ #Usamos otro list_comprehesion para filtrar los estudiantes que no lleguen al promedio
            estudiante
            for estudiante in lista_comprehesion
            if estudiante.average_grade() >= promedio
        ]

        aprobados = { #Finalmente hacemos otro list_comprehesion para dejar los estudiantes que tienen una nota mayor o igual al promedio
            estudiante.name: estudiante
            for estudiante in filtrado
        }

        return aprobados

Actividad_POO()

