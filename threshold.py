"""batteries=[50,30,4,45,12,18,30]
mimimal=20
usable=0
count=0
for battery in batteries:
    if battery > mimimal:
        usable += battery
        count = count + 1

print(usable,count)



alien="uoy erutpac anoog era ew namuh ih"
print(alien)
human=alien[::-1]
print(human)

available=[
 "apple",
 "banana",
 "kiwi",
 "kit kat",
 "grapes",
 "water",
 "berry",
]
crew=4
each=len(available) // crew
remaining=len(available) % crew
print("each crew gets:",{each}," and remaining:",{remaining})

"""

def setup_mission():
    print("setting up the mission")
    available=[
 "apple",
 "banana",
 "kiwi",
 "kit kat",
 "grapes",
 "water",
 "berry",
]
    crew_available=int(input("enter the num of crew"))
    print("setup completed")
    return crew_available,available
    
    

def freedom_game():
    print("Weelcome to the world of Survival")
    print("mission started............")

    crew_number,food=setup_mission()
    print(f"you have= {crew_number}","and number of foods ={food}")
    
    print("welcome to mars!!!!")
    print("your battery is dead plese charge")
    batteries=[50,30,4,45,12,18,30]
    mimimal=20
    usable=0
    count=0
    for battery in batteries:
     if battery > mimimal:
        usable += battery
        count = count + 1
        print(usable,count)
    
print("mission completed")



freedom_game()



   

