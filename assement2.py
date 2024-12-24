"""my_list=[1, 2, 3, 'a', 'b', 'c']
my_list.append('d')
my_list.remove(2)
print(len(my_list))
print(my_list)

my_tuple=(10, 20, 30, 40, 50)
print(my_tuple[2])
l_1=list(my_tuple)
l_1[3]=35
p_1=tuple(l_1)
print(p_1)

my_set={1, 2, 2, 3, 4, 4, 5}
my_set.add(6)
my_set.remove(3)
print(my_set)
print(4 in my_set)"""


my_dict={'name': 'John', 
         'age': 25, 
         'city': 'New York'}
my_dict["job"]="Engineer"
my_dict.update({'age':26})
my_dict.pop("city")
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
print(my_dict)

def palindrome(string):
    if string in ('aca' ,'aabbaa'):
        return True
    elif  string in ("abbbb" ,"baabbb"):
          return False
    else:
         return None

result=palindrome('aca')
print(result)

radius=int(input("enter the radius"))
pie=3.14
area=pie *radius *radius
print(area)


    



