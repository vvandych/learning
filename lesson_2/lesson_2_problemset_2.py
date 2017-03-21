#weekend

def weekend(day):
    if day=='Saturday' or day=='Sunday':
        return True
    if day!='Saturday' or day!='Sunday':
        return False
    else:
        return day
print weekend('Monday')
print weekend('Saturday')
print weekend('July')



#stamps
def stamps(a):
    while True:
      b=int (a/5)
      break
    while True:
        c=int ((a-b*5)/2)
        break
    while True:
        d=int ((a-5*b-2*c)/1)
        break
    return b,c,d
print stamps(8)
print stamps(5)
print stamps(29)
print stamps(0)



#last
def set_range(a,b,c):
   d=max (a,b,c)
   e=min (a,b,c)
   return d-e


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1/4 !=int:
        daysOfMonthsy1 =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year2/4 !=int:
        daysOfMonthsy2 =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        daysOfMonthsy1=daysOfMonthsy2 =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    years=year2-year1
    days_in_monthes=sum(daysOfMonthsy2[:month2-1])-sum(daysOfMonthsy1[:month1-1])
    days=day2-day1
    all_days=years*365+days_in_monthes+days
    return all_days
print daysBetweenDates(2012,1,1,2012,2,28)