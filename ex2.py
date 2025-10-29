import random

def get_numbers_ticket(a:int, b:int, q:int ):
    try:
        if q > (b - a + 1) or a<0 or b>1000 or q>1000 or q<0:
           return []
    except (ValueError,TypeError):
        return [] 
    else:   
        unique=set()
       
        while len(unique) < q:
            unique.add(random.randint(a,b)) 

        lst=sorted(list(unique))
             

        return lst    
       
    
    
       
print(get_numbers_ticket(10,14,6))


