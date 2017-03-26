
def greatest(list_of_numbers):
    p=list_of_numbers
    if len(p)==0:
        return 0
    else:
        p.sort()
        a=p.pop()
    return a