

class GradeCalculator:
    def __init__(self, points):
        self.points = points
        self.grade = None
        self.points_list = []

    def getGrade(self, points):
        try:
            if points < 0 or points > 100:
                raise ValueError
            self.points = points
            if self.points < 0 or self.points > 100:
                return ValueError
            elif self.points <= 44:
                return 'F'
            elif self.points <= 59:
                return 'D'
            elif self.points <= 74:
                return 'C'
            elif self.points <= 89:
                return 'B'
            else:
                return 'A'
        except ValueError:
            return ValueError
        except TypeError:
            return TypeError

    def is_passed(self, points):
        try:
            self.points = points
            if self.points > 45 and 101 > self.points:
                return True
            elif self.points >= 0 and self.points <= 45:
                return False
        except ValueError:
            if self.points < 0 or self.points > 100:
                return ValueError
        except TypeError:
            return TypeError

    def get_average(self, points_list):
        try:
            self.points_list = points_list
            result = sum(self.points_list) / len(self.points_list)
            return float(result)
        except ValueError:
            if points_list < 0 or points_list > 100:
                return ValueError
        except TypeError:
            return TypeError

