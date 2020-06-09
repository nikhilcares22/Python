month_days =[0,31,30,31,30,31,30,31,31,30,31,30,31]
"""Days in months for indexing purpose and first value is place holder"""
def is_leap_year(year):
    return year % 4==0 and(year % 400 == 0 or year % 100 != 0)
def month_in_year(year,month):
    if not 1<=month<=12:
        return'Invlaid Month'
    if month==2 and is_leap_year(year):
        return 29
    return month_days[month]
print(is_leap_year(2020))