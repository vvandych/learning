l = "she sells seashells by the seashore"
def find_second(l,a):
   number = l.find(a)   
   final_number = l.find(a,number+1)
   return final_number
print find_second(l,'she')




def bigger(x,y):
    if x<y:
            return y
    else:
            return x
print bigger(4,5)




def is_friend(name):
    if name.find('D')==0:
      x=True
    else:
      x=False
    return x
print is_friend('Diana')
#otherway
def is_friend(name):
    if name[0]=='D':
        return True
    else:
        return False
print is_friend('Diana')
#otherway1
def is_friend(name):
     return name[0]=='D'
print is_friend('Diana')



#не робочий варіант
def is_friend(name):
     x='D'
     z='N'
     if name[0]==x:
                 y=True
     else:
                 y=False
     return y
print is_friend('Mark')
#робочий варіант
def is_friend(name):
     let='DN'
     if let.find(name[0])>=0:
                       y=True
     else:
                       y=False
     return y
print is_friend('Mark')



#quiz biggest

def biggest(a,b,c):
    if a>=b and a>=c:
       return a
    if b>=a and b>=c:
        return b
    if c>=a and c>=b:
        return c
print biggest(6,3,9)
#2way
def bigger(a,b):
               if a>b:
                      return a
               else:
                      return b
def biggest(a,b,c):
     if bigger(a,b)<c:
                      return c
     else:
                      return bigger(a,b)
print biggest(1,2,3)



#quiz while looops
def numbers(n):
 i=1
 while i<=n:
           print i
           i=i+1
print numbers(3)



#factorial
def factorial(n):
   result=1
   while n>=1:
       result=result*n
       n=n-1
   return result
print factorial(2)




#mulltiple assigment
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link<0:
                    url,end_quote=None,0
    else:
         start_quote = page.find('"', start_link)
         end_quote = page.find('"', start_quote + 1)
         url = page[start_quote + 1:end_quote]
    return url, end_quote
url,endpos=get_next_target('mood')   
def print_all_links(page):
    while True:
        url,nextpos=get_next_target(page)
        if url:
            print url
            page=page[endpos:]
        else:
          break

