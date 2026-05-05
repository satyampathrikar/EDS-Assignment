players = {}

n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    height = float(input("Enter height (cm): "))
    players[name] = height

captain = max(players, key=players.get)

print("Team Players:", players)
print("Captain (Tallest Player):", captain)