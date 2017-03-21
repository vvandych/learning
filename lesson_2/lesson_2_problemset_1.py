#quiz udacify
def udacify(name):
    return 'U'+name
print udacify('dacians')



#quiz median
def median(a,b,c):
    if a<=b<=c or c<=b<=a:
        return b
    if b<=c<=a or a<=c<=b:
        return c
    if b<=a<=c or c<=a<b:
        return a
print median(3,2,3)



#quiz blastoff
def countdown(z):
    print z
    while z>1:
        z=z-1
        print z
        if z==1:
                break
    print 'Blastoff!'                      
print countdown(3)

#quiz find last
def find_last(search_str,thing_2_search):
     n==-2
 while n < len(search_str):
     n=n+1
 if n<len(z):
            z=search_str.find(thing_2_search,n)
 print max (z)
print find_last('aaaa','a')
