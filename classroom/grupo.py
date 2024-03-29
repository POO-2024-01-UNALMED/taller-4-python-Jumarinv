from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas= None, estudiantes = None):
        if asignaturas == None:
            asignaturas = []
        if estudiantes == None:
            estudiantes = []
        self._grupo = grupo
        print(self._grupo)
        self._asignaturas = asignaturas
        print(self._asignaturas)
        self.listadoAlumnos = estudiantes
        print(self.listadoAlumnos)

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        
        return(f"Grupo de estudiantes: {self._grupo}")

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
