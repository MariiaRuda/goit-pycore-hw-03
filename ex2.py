import random

def get_number_ticket(a:int, b:int, q:int ):
    if type(a) is int and type(b) is int and type(q) is int:
            
            if a<0 or b>1000 or q>1000 or q<0:
                print("valid range is between 1(a) and 1000(b)," \
                  "quantity of numbers is between 1(q) and 1000(q)")
            else:
                unique=set()
                for i in range(q):
                     unique.add(random.randint(a,b)) 

                lst=list(unique)
                lst.sort()      
                print(f"This is sorted unique winning sequence: {lst}")     
    else:
       print("please enter values of type int")
    
get_number_ticket(10,150,4)