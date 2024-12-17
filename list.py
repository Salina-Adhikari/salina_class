fruits=["mango","banana","cherry"]
fruits.insert(3,"lemon")

fruits.append("pappaya")
for fruit in fruits:
 print(fruits)

 for index,fruit in enumerate(fruits):
  print(f"Item position:{index} and value:{fruit}")

  #unpack 
  (green,yellow,*red)=fruits
  print(green,yellow,red)   #* sign all the remaining goes

  f_1={"red","yellow","blue"}

for item in f_1:
   print(item)

f_1.add("sage")
print(f_1)