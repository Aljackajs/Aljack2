def days_between_dates(date1, date2):
    d1, m1, y1 = date1
    d2, m2, y2 = date2

    days1 = y1 * 365 + (y1 // 4) - (y1 // 100) + (y1 // 400) + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, d1 - 1])
    if m1 <= 2:
        days1 -= 1
    days2 = y2 * 365 + (y2 // 4) - (y2 // 100) + (y2 // 400) + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, d2 - 1])
    if m2 <= 2:
        days2 -= 1

    return abs(days2 - days1)

date1 = (10, 4, 2023)  
date2 = (15, 8, 2024)

# Find the number of days between the two dates
days_difference = days_between_dates(date1, date2)
print("Number of days between the two dates:", days_difference)
