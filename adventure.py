import time

# Initialize pet stats (default values)
pet_name = ""
hunger = 50
happiness = 50
energy = 50

# Define the pet actions
def feed_pet():
    global hunger
    hunger = min(hunger + 20, 100)
    print(f"\n{pet_name}'s hunger increased to {hunger}.")

def play_pet():
    global happiness, energy
    happiness = min(happiness + 20, 100)
    energy = max(energy - 20, 0)
    print(f"\n{pet_name}'s happiness increased to {happiness} and energy decreased to {energy}.")

def rest_pet():
    global energy, hunger
    energy = min(energy + 20, 100)
    hunger = max(hunger - 5, 0)
    print(f"\n{pet_name}'s energy increased to {energy} and hunger decreased to {hunger}.")

def pet_status():
    print(f"\n{pet_name}'s Status:")
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")
    print(f"Energy: {energy}")

# Define the pet game loop
def pet_game():
    global pet_name, hunger, happiness, energy

    # Ask for the pet name if it's not already set
    if not pet_name:
        pet_name = input("\nEnter your pet's name: ").strip()
        hunger, happiness, energy = 50, 50, 50  # Initialize stats

    print("\nWelcome to the Pet Game!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the pet")
        print("2. Let the pet play")
        print("3. Let the pet rest")
        print("4. Quit and return to the main menu")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            feed_pet()
        elif choice == "2":
            play_pet()
        elif choice == "3":
            rest_pet()
        elif choice == "4":
            print(f"\nReturning to the main menu. Thanks for playing, {pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main menu
def main():
    while True:
        print("\n== Adventure Game ==")
        print("1. Pet Game")
        print("2. View Your Pet's Status")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            pet_game()
        elif choice == "2":
            if pet_name:
                pet_status()
            else:
                print("\nYou need to start the pet game first!")
        elif choice == "3":
            print("You exited the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
