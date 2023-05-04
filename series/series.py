
    
def fibonacci(n):
    '''
        this function calculate the fibonacci for anumber 
         :param n:int
         :return: int
    '''
    
    if type(n) != int:
        return   "please add number"
    else:
        if n==0  :
            return   0
        elif n==1 or n==2 :
            return 1
        else :
            return fibonacci(n-1) +fibonacci(n-2)


def lucas(n):
    '''
        this function calculate the lucas for anumber 
         :param n:int
         :return: int
    '''
    if type(n) != int:
        return   "please add number"
    else:
        if n==0  :
            return   2
        elif n==1 :
            return 1
        else :
            return lucas(n-1)+lucas(n-2)


def sum_series(n,x=0,y=1):
    '''
        this function calculate the sum_series for anumber 
         :params n,x,y:int
         :return: int
    '''
    if type(n) != int:
        return   "please add number"
    if x==0 and y==1:
       return fibonacci(n)
         
    elif x==2 and y==1 :
       return lucas(n)
    else :
        
        if n==0  :
            return   x
        elif n==1 :
            return y
        else :
            return sum_series(n-1,x,y)+sum_series(n-2,x,y)

