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