def fix_machine(debris, product):
    pos=0
    lens=len(product)
    while pos<lens:
        check=debris.find(product[pos])
        if check==-1:
            return "Give me something that's not useless next time."
        pos=pos+1
    return product
print fix_machine('UdaciousUdacitee', 'Udacity') 
print fix_machine('buy me dat Unicorn', 'Udacity') 
print fix_machine('AEIOU and sometimes y... c', 'Udacity') 


#days old
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1/4==int:
        daysOfMonthsy1 =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year2/4==int:
        daysOfMonthsy2 =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        daysOfMonthsy2 =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        daysOfMonthsy1 =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    years=year2*sum(daysOfMonthsy2)-year1*sum(daysOfMonthsy1)
    if year2-year1>=4:
        leapy=int (year2-year1)/4
    else:
        leapy =0
    if day1==day2:
        days=day2-day1+1
    else:
        days=day2-day1
    days_in_monthes=sum(daysOfMonthsy2[:month2-1])-sum(daysOfMonthsy1[:month1-1])
    all_days=years+days_in_monthes+days+leapy
    return all_days


def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
