class School:
    def __init__(self, school_name):
        self.school_name = school_name
        print("School init called")

class Grade:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print("Grade class init called")

class SportsTeam:
    def __init__(self, sport_name):
        self.sport_name = sport_name
        self.team = []

    def add_player(self, player_name):
        self.team.append(player_name)

class Student(School, Grade, SportsTeam):
    def __init__(self, name, grade_name, school_name, sport_name):
        self.name = name
        print("Student init called")
        Grade.__init__(self, grade_name)
        School.__init__(self, school_name)
        SportsTeam.__init__(self, sport_name)


antar = Student("Antar", "Bsc", "FEC", "cricket")
print(antar.name)
print(antar.grade_name)
print(antar.school_name)
print(antar.sport_name)
antar.add_player("Arnob")
antar.add_player("Antar")
print(antar.team)

