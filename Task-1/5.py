total_days=int(input("Enter total days: "))
year=total_days//365
weeks=(total_days%365)//7
days=(total_days%365)%7
print(year,"year",weeks,"week",days,"days")
