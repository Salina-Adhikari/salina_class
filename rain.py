"""def multiplication(*args):
    result=1
    for number in args:
        result*=number
    
    return result
    
def sum(*args):
    result=0
    for number in args:
        result+=number
        
    return result"""
    


def student(*args,**kwargs):
    
    result=0
    for number in args:
       result+=number
    print(f"Full Name is {kwargs['F_name']} {kwarg['l_1']} and total marks is")
student(20,20,40,f_1="salina adhikari",l_1="adhikari")
    