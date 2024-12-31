"""class Car:
    def __init__(self,color,model):
        self.color=color
        self.model=model

lambo=Car("Red","2023")
print(lambo.color)
print(lambo.model)"""

class PhoneFactory:
    model:None
    color:None
    is_android:None

    def __init__(self,model,color,is_android):
      
        self.model=model
        self.color=color
        self.is_android=is_android

    def __str__(self):
        return f"{self.model}.{self.color}"
    
    def check_os(self):
        if self.is_android:
            print("It is android")
        else:
            print("ios")

Samsung=PhoneFactory("a56","Red",True)
Samsung.model="a56"
Samsung.color="Red"
Samsung.is_android=True

print(Samsung.PhoneFactory)