delays = {
    "F101": [10, 15, 5],
    "F202": [30, 25],
    "F303": [5, 10],
    "F404": [40, 35, 45]
}

avg_delay={}
for flight, mins in delays.items():
    avg_delay[flight]=sum(mins) / len(mins)
print("Average delay per flight:", avg_delay)

worst_flight=max(avg_delay, key=avg_delay.get)
print("Flight with highest average delay:", worst_flight)
print("Highest average delay:", avg_delay[worst_flight])
