# 1. The Adventure Game
# Task 1.Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":  # Task 2. Setting the Scene
   action = input("light a torch or proceed in the dark?")
   if action == "light a torch":
       print("Explore the cave!")
   elif action == "proceed in the dark":
        print("Enter the cave and fall to your DEATH!")
elif place == "Bunker": # Task 3. The PASS
            pass
    
# 2. The Event Planner
# Task 1. Code Correction

attendees = int(input("Enter number of attendees:"))
venue = "Large Hall" if attendees > 100 else "Conference Room"
print(venue)
if attendees > 150: # Task 2. Venue Selection
    action = input("Would you like a PA? ")
    if action == "yes":
        print("PA will be set up for you")
    else:
        print("Hope you can YELL!")
    action = input("How about a projector? ")
    if action == "yes":
         print("Projector will be set up and focused")
    else:
         print("Your on your own kiddo!")
meal = input("Would you like a vegetarian meal?")
if action == "yes":
     print("We recommend 'Veggie Delight Caterers'")
else:
     print("We recommend 'Gourmet Meals Caterers'")



