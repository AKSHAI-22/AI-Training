leaderboard = [
    ("Akshai", 150),
    ("Ravi", 200),
    ("Sneha", 180),
    ("Akshai", 170),
    ("Kiran", 160)
]
seen=set()
valid=[]
invalid=[]
for player, score in leaderboard:
    if player in seen:
        invalid.append((player, score))
    else:
        seen.add(player)
        valid.append((player, score))

print("Invalid entries:", invalid)
final_board = sorted(valid, key=lambda x: x[1], reverse=True)
print("Final leaderboard:", final_board)
