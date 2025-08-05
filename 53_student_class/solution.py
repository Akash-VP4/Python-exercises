class Parant:
    def __init__(self, name):
        self.name = name
        self.child = []

    def add_child(self, value):
        self.child.append(value)

    def get_mean(self):
        mean = 0
        for value in self.child:
            mean += value.get_mean()

        return mean / len(self.child)

    def get_best_child(self):
        best_child = self.child[0]
        for val in self.child:
            if val.get_mean() > best_child.get_mean():
                best_child = val
        return best_child


class Student(Parant):

    def add_exam(self, grade):
        self.add_child(grade)

    def get_mean(self):
        return sum(self.child) / len(self.child)


class School(Parant):

    def add_student(self, student):
        self.add_child(student)

    def get_best_student(self):
        return self.get_best_child()


class City(Parant):

    def add_school(self, school):
        self.add_child(school)

    def get_best_school(self):
        return self.get_best_child()

    def get_best_student(self):
        schl = self.child[0]
        for school in self.child:
            if (
                school.get_best_student().get_mean()
                > schl.get_best_student().get_mean()
            ):
                schl = school
        return schl.get_best_student()
