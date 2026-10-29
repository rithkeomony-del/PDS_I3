# a. Write is_leap(year) that returns True or False
def is_leap(year):
    return (year % 4 == 0 and year % 100 !=0 ) or (year  %  400 == 0)

# b. Write days_in_month(month, year) that returns 28, 29, 30 or 31, or None
def days_in_month(month, year):
    if (month < 1 or month >12) and year > 0:
        return None
    elif month == 2:
        if is_leap(year) :
            return 29
        return 28
    elif month in (4, 6, 9, 11):
        return 30
    return 31

print(f"Feb 2024: {days_in_month(2, 2024)} | Feb 2026: {days_in_month(2, 2026)} | Apr: {days_in_month(4, 2024)} | month 13: {days_in_month(13, 2024)}")

# c. print if leap year
years = [1900,2000,2024,2026]

for year in years :
    if is_leap(year) :
        print(f"{year} is a leap year.")
    else :
        print(f"{year} is not a leap year.")
        
# d. Count leap year using loop
count = 0
for year in range(1999,2101):
    if is_leap(year):
        count += 1
print(f"leap years from 2000 to 2100 : {count}")