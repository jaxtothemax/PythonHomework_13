class BasketballPlayer():
    def __init__(self, team, first_name, last_name, height_cm, weight_kg, points, rebounds, assists, triple_doubles):
        self.team = team
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_cm = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.triple_doubles = triple_doubles


print("Build your own NBA team with adding your own favorite players!")

new_player = BasketballPlayer(
    team=input("Enter player team: "),
    first_name=input("First name: "),
    last_name=input("Last name: "),
    height_cm=input("Height in centimeters: "),
    weight_kg=input("Weight in kilograms: "),
    points=input("Points: "),
    rebounds=input("Rebounds: "),
    assists=input("Assists: "),
    triple_doubles=input("Triple doubles: ")
)

with open("player.txt", "w") as player_file:
    player_file.write(str(new_player.__dict__))

print("Player added!")