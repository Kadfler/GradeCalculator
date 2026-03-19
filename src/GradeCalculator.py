class GradeCalculator:
    def __init__(self, points):
        self.points = points
        self.grade = None
        self.points_list = []

    def getGrade(self, points):
        self.points = points
        if self.points < 0 or self.points > 100:
            return ValueError
        elif self.points <=44:
            return 'F'
        elif self.points <=59:
            return 'D'
        elif self.points <=74:
            return 'C'
        elif self.points <=89:
            return 'B'
        else:
            return 'A'

    def is_passed(self):
        try:
            if self.points > 45:
                return True
            else:
                return False
        except ValueError:
            return ValueError

    def get_average(self, points_list) -> float:
        try:
            self.points_list = points_list
            return sum(self.points_list) / len(points_list)
        except ValueError:
            if points_list <0 or points_list > 100:
                return ValueError

student1 = GradeCalculator(-1)
print(f"Оценка: {student1.getGrade(student1.points)}")