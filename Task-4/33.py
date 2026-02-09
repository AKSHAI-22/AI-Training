shows = {
    "10AM": {1, 2, 3, 4},
    "1PM": {1, 2, 3, 4},
    "4PM": {2, 3, 4},
    "7PM": {1, 2, 3, 4}
}
total_seats = {1, 2, 3, 4}
full=[]
for time,show in shows.items():
    if show==total_seats:
        full.append(time)
print("Fully booked seats:",full)

seats=list(shows.values())
common=seats[0]

for s in seats[1:]:
    common=common.intersection(s)
print(common)

