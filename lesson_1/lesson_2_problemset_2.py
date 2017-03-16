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
