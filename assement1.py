num1=int(input("Enter a number"))
double=num1*2
print(double)
a=double+10
print(a)
y=a/2
print(y)
sub=y-num1
print(sub)

#Temperature(Celsius-Fehereneith)

cel=float(input("Enter the celsius"))
feh=(cel*9/5)+32
print("The temperature is:",feh)

meter=int(input("enter the length in meter"))
kilometer=meter/1000
print("The length in kilometer is :",kilometer)

feet=int(input("enter your height"))
inches=int(feet*12)
print("Your height in inches is:",inches)

Dollar=float(input("enter the currency of your USA"))
Rupees=Dollar*135.746 
print("Your amount in rupees",Rupees)


principal=float(input("Enter the principle"))
time=float(input("enter the number of years"))
rate=float(input("enter the rate of interst"))
SI=(principal*time*rate)/100
print(SI)


Principal=float(input("enter the principal"))
rate=float(input("Enter the rate"))
Rate=rate/100
number=int(input("Enter the number of times the interest is compunded every year"))
Time=int(input("enter years"))
Amount=Principal*(1+Rate/number)**(number*Time)
CI=Amount-Principal
print(f"Your compount interest is: {CI:.2f}")

rectangle_length=float(input("enter the lenght"))
rectangle_breadth=float(input("enter the breath"))
perimeter=2*(rectangle_length+rectangle_breadth)
area=rectangle_breadth*rectangle_length
print(perimeter,area)

radius=float(input("enter the radius"))
pie=3.14
circle_perimeter=2*radius*pie
circle_area=radius*radius*pie
print(circle_area,circle_perimeter)

a_1=int(input("enter the a side"))
a_2=int(input("enter the b side"))
a_3=int(input("enter the c side"))
height=int(input("enter the height"))
triangle_area=(height*a_1)*1/2
triangle_perimeter=a_1+a_2+a_3
print(triangle_area,triangle_perimeter)

num1=int(input("Enter a number"))
if num1 % 2==0:
    print("even")

else:
    print("odd ")

num2=int(input("enter a number"))
for i in range(2,num2):
    if num2 % i==0:
        print("Not prime")
        break
    else:
        print("Prime")

num3=int(input("enter the number"))
num4=int(input("enter another number"))

if num3 %  num4 == 0:
        print(" the number is divisible ")
else:
        print("it is not divisible ")
 
while True:
     user_choice=input(""" 
1. km to miles
2.miles to km
3.centimeter to inch
4.inch to centimeter
""")
     if user_choice=="1":
      cel=float(input("Enter the celsius"))
      feh=(cel*9/5)+32
      print("The temperature is:",feh)
      
     elif user_choice=="2":
       meter=int(input("enter the length in meter"))
       kilometer=meter/1000
       print("The length in kilometer is :",kilometer)

     elif user_choice=="3":
      feet=int(input("enter your height"))
     inches=int(feet*12)
     print("Your height in inches is:",inches)
else :
     Dollar=float(input("enter the currency of your USA"))
     Rupees=Dollar*135.746 
     print("Your amount in rupees",Rupees)

one=int(input("enter the number"))
for i in range(1,one):
    if i*i==one:
        print("the number is square:",i)
        break
else:
        print("the number is not square number")

