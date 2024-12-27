# Members: Mirafuentes, Jerson A. ---- Remotigue, Niel Angelo L.
import sys
import time

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

# Initialize player health and skills
def initialize_game():
    player = {
        "health": 100,
        "skills": {
            "fireball": 3,
            "defensive_shield": 2,
            "dash_movement": 3
        },
        "has_reached_safety": False
    }
    return player

def use_skill(player, skill):
    if player["skills"].get(skill, 0) > 0:
        player["skills"][skill] -= 1
        return True
    else:
        print_slow("You are out of uses for this skill!")
        return False

def main():
    player = initialize_game()
    print_slow("Welcome to the Dark Lands, traveler. You find yourself in a desolate forest, shrouded in mist...")
    time.sleep(1)

    while player["health"] > 0 and not player["has_reached_safety"]:
        try:
            print_slow(f"\nYour current health: {player['health']}")
            print_slow(f"Skills available: Fireball({player['skills']['fireball']}), Defensive Shield({player['skills']['defensive_shield']}), Dash Movement({player['skills']['dash_movement']})")
            print("Do you wish to: ")
            print("1. Venture deeper into the forest")
            print("2. Follow the sound of running water")
            print("3. Light a torch and stay put")
            print("4. Climb a nearby tree to get your bearings")
            print("5. Look for shelter to rest until dawn")
            print("6. Quit the game")

            choice1 = int(input("Enter your choice (1-6): "))

            if choice1 == 1:
                forest_path(player)
            elif choice1 == 2:
                river_path(player)
            elif choice1 == 3:
                stay_put(player)
            elif choice1 == 4:
                climb_tree(player)
            elif choice1 == 5:
                find_shelter(player)
            elif choice1 == 6:
                print_slow("Thank you for playing. Farewell, brave soul.")
                break
            else:
                print_slow("Please choose a valid option (1-6).")
        except ValueError:
            print_slow("Invalid input! Please enter a number between 1 and 6.")

    if player["has_reached_safety"]:
        print_slow("Congratulations! You have reached safety and survived the Dark Lands. The game is over.")
    elif player["health"] <= 0:
        print_slow("You succumbed to the dangers of the Dark Lands. Game Over.")

def forest_path(player):
    print_slow("\nYou tread deeper into the forest. Shadows seem to close in around you.")
    time.sleep(1)
    print("A dark figure cloaked in rags blocks your way.")

    while True:
        try:
            print("Do you: ")
            print("1. Offer some coins")
            print("2. Refuse and draw your weapon")
            print("3. Use Fireball")
            print("4. Use Defensive Shield")
            print("5. Use Dash Movement")
            
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                print_slow("The figure accepts your offering and vanishes. You proceed safely.")
                break
            elif choice == 2:
                print_slow("The figure reveals itself as a wraith and strikes you.")
                player["health"] -= 30
                if player["health"] <= 0:
                    print_slow("You succumb to your injuries. Game Over.")
                    return
            elif choice == 3:
                if use_skill(player, "fireball"):
                    print_slow("You cast Fireball, incinerating the figure. You proceed safely.")
                    break
            elif choice == 4:
                if use_skill(player, "defensive_shield"):
                    print_slow("You block the wraith's attack with a Defensive Shield and escape safely.")
                    break
            elif choice == 5:
                if use_skill(player, "dash_movement"):
                    print_slow("You use Dash Movement to evade the figure and escape safely.")
                    break
            else:
                print_slow("Please choose a valid option (1-5).")
        except ValueError:
            print_slow("Invalid input! Please enter a number between 1 and 5.")

def river_path(player):
    print_slow("\nYou follow the sound of running water and come upon a swift river.")
    time.sleep(1)
    print("A bridge lies ahead, but it looks unstable. You also notice a small boat by the shore.")

    while True:
        try:
            print("Do you: ")
            print("1. Cross the bridge")
            print("2. Take the boat")
            print("3. Turn back to the forest")
            print("4. Use Dash Movement to leap across the river")
            print("5. Search for a nearby crossing")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                print_slow("The bridge collapses halfway. You fall into the river and are swept away. Game Over.")
                player["health"] = 0
                return
            elif choice == 2:
                print_slow("The boat carries you safely to the other side. You find a small village and reach safety.")
                player["has_reached_safety"] = True
                return
            elif choice == 3:
                print_slow("You decide the river is too risky and return to the forest path.")
                forest_path(player)
                return
            elif choice == 4:
                if use_skill(player, "dash_movement"):
                    print_slow("You use Dash Movement to leap across the river, reaching the other side safely.")
                    player["has_reached_safety"] = True
                    return
            elif choice == 5:
                print_slow("You find a fallen tree nearby and use it to cross safely. You survive!")
                player["has_reached_safety"] = True
                return
            else:
                print_slow("Please choose a valid option (1-5).")
        except ValueError:
            print_slow("Invalid input! Please enter a number between 1 and 5.")

def stay_put(player):
    print_slow("\nYou decide to light a torch and stay where you are.")
    time.sleep(1)
    print("Suddenly, you notice a pair of glowing eyes in the darkness watching you.")

    while True:
        try:
            print("Do you: ")
            print("1. Approach the eyes")
            print("2. Shout to scare it off")
            print("3. Use Fireball")
            print("4. Use Defensive Shield")
            print("5. Hide and observe silently")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                print_slow("You approach and discover it's a large wolf. It attacks before you can react. Game Over.")
                player["health"] = 0
                return
            elif choice == 2:
                print_slow("Your shout startles the creature, which runs off. You find a safer path and reach a nearby village.")
                player["has_reached_safety"] = True
                return
            elif choice == 3:
                if use_skill(player, "fireball"):
                    print_slow("You cast Fireball, scaring the wolf away. You proceed safely.")
                    player["has_reached_safety"] = True
                    return
            elif choice == 4:
                if use_skill(player, "defensive_shield"):
                    print_slow("The Defensive Shield protects you as the wolf retreats. You survive.")
                    player["has_reached_safety"] = True
                    return
            elif choice == 5:
                print_slow("You hide silently, watching as a pack of wolves passes by. Once they’re gone, you move to safety.")
                player["has_reached_safety"] = True
                return
            else:
                print_slow("Please choose a valid option (1-5).")
        except ValueError:
            print_slow("Invalid input! Please enter a number between 1 and 5.")

def find_shelter(player):
    print_slow("\nYou look for shelter to rest until dawn.")
    time.sleep(1)
    print("You find an abandoned hut nearby. As you enter, you notice strange symbols on the walls.")

    while True:
        try:
            print("Do you: ")
            print("1. Explore the hut further")
            print("2. Rest by the door")
            print("3. Light a fire to keep warm")
            print("4. Cover the symbols with cloth")
            print("5. Leave the hut and continue your journey")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                print_slow("You trigger a trap and the door seals shut. Game Over.")
                player["health"] = 0
                return
            elif choice == 2:
                print_slow("You rest lightly and make it through the night safely.")
                player["has_reached_safety"] = True
                return
            elif choice == 3:
                print_slow("The fire illuminates hidden symbols, revealing a way out. You survive!")
                player["has_reached_safety"] = True
                return
            elif choice == 4:
                print_slow("You cover the symbols, and the room feels safer. You sleep and make it through the night.")
                player["has_reached_safety"] = True
                return
            elif choice == 5:
                print_slow("You leave and continue through the forest, eventually reaching a village.")
                player["has_reached_safety"] = True
                return
            else:
                print_slow("Please choose a valid option (1-5).")
        except ValueError:
            print_slow("Invalid input! Please enter a number between 1 and 5.")

def climb_tree(player):
    print_slow("\nYou climb a nearby tree to get a better view.")
    time.sleep(1)
    print("From the treetop, you see smoke rising in the distance and movement below.")

    while True:
        try:
            print("Do you: ")
            print("1. Climb down and head toward the smoke")
            print("2. Stay in the tree and rest")
            print("3. Jump to another tree to explore further")
            print("4. Drop a branch to test if anything reacts below")
            print("5. Use your vantage point to scout for threats")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                print_slow("You reach a small camp with friendly travelers who offer you food and shelter. You survive!")
                player["has_reached_safety"] = True
                return
            elif choice == 2:
                print_slow("You fall asleep but awaken to a predator below. It’s too late to escape. Game Over.")
                player["health"] = 0
                return
            elif choice == 3:
                print_slow("You slip while jumping and fall, injuring yourself. Game Over.")
                player["health"] = 0
                return
            elif choice == 4:
                print_slow("The noise startles a bear, which leaves the area. You climb down and escape safely.")
                return
            elif choice == 5:
                print_slow("You notice a clear path that leads to safety and descend to follow it. You survive!")
                player["has_reached_safety"] = True
                return
            else:
                print_slow("Please choose a valid option (1-5).")
        except ValueError:
            print_slow("Invalid input! Please enter a number between 1 and 5.")

# Start the game
if __name__ == "__main__":
    main()
