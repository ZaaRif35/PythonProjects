class JocuriV:
        def __init__(self, name, realese_age, game_type):
            self.name = name
            self.realese_age = realese_age
            self.game_type = game_type

JV = JocuriV("Fallout 3", 2008, "Adventure,Post.Apocalipcis")

print(JV.name)
print(JV.realese_age)
print(JV.game_type)