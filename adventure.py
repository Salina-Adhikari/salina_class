import time



class Pet:
    def __init__(self, name):
        self.pet_name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
   

    def is_sick(self):
        if (self.hunger==0 or self.happiness==0 or self.energy==0):
            return True
        else:
            return False
       
    

    def feed_pet(self):
        self.hunger = min(self.hunger + 20, 100)
        print(f"\n{self.pet_name}'s hunger increased to {self.hunger}.")
        

    def play_pet(self):
        self.happiness = min(self.happiness + 20, 100)
        self.energy = max(self.energy - 20, 0)
        print(f"\n{self.pet_name}'s happiness increased to {self.happiness} and energy decreased to {self.energy}.")
       



    def rest_pet(self):
        self.energy = min(self.energy + 20, 100)
        self.hunger = max(self.hunger - 5, 0)
        print(f"\n{self.pet_name}'s energy increased to {self.energy} and hunger decreased to {self.hunger}.")
        
    def pet_status(self):
        print(f"\n{self.pet_name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

  
def pet_game(pet):
    while True:
        if pet.is_sick():
            print("thank you for playing")
            break

        
          

        # Game menu
        print("\n== Update the Pet ==")
        print("1. Feed the Pet")
        print("2. Play with Pet")
        print("3. Rest Time")
        print("4. Exit to Main Menu")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            pet.feed_pet()
        elif choice == "2":
            pet.play_pet()
        elif choice == "3":
            pet.rest_pet()
        elif choice == "4":
            print(f"\nReturning to the main menu, {pet.pet_name}!")
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")


def main():
    pet = None
    while True:
        print("\n== Adventure Game ==")
        print("1. Pet Game")
        print("2. View Your Pet's Status")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            if not pet:
                pet_name = input("\nEnter your pet's name: ").strip()
                pet = Pet(pet_name)
            pet_game(pet)
        elif choice == "2":
            if pet:
                pet.pet_status()
            else:
                print("\nYou need to start the pet game first!")
        elif choice == "3":
            print("You exited the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

