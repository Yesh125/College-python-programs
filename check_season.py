month = int(input("Enter the month (as a number): "))

def check_season(month):
 if(month == 2 or month==3):
  return "Spring"
 elif month == 4 or month== 5 or month==6:
  return "Summer"
 elif month == 7 or month ==8 or month==9 or month == 10:
  return "Autumn"
 elif month ==11 or month == 12 or month==1:
  return "Winter"
 else:
  return "Invalid month"
print("Season:", check_season(month))