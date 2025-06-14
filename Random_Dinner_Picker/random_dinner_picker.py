import random

def food_choice():
    foods = ["biryani", "ghee rice", "porota", "chapathi", "kushka"]
    print("What do you want for the day ?")
    input("Press Enter to get your food suggestion...") 
    choice=random.choice(foods)
    return choice 

food=food_choice()
print(f"Here is your food for the day {food}, Bon Apetite!")
    
    
# This code randomly selects a food item from a predefined list and suggests it to the user.
# It prompts the user to press Enter to receive the suggestion, making it interactive.
# The list of foods can be modified to include any items you prefer.
# The final print statement displays the selected food item in a friendly manner.
# This code is a simple food suggestion program that randomly selects a food item from a predefined list.