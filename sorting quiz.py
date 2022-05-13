# ask user a series of questions with corresponding house sorting
# account for each answer and its corresponding house
# tally houses and declare the users house


name = input("What's your name?\n")
hogwarts_house = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]


sorting_name = f"Hello, {name}! Welcome to the Sorting Hat..."

print(sorting_name)
print("Answer each question to find your Hogwarts House!")


sorting_hat_file = open("sortingquestions.txt", "r")
line = sorting_hat_file.readline()
sortingquestion = line.split(",")

HogwartsHouse = [] # list of each house answer 

while sortingquestion[0] != "END":
    print(sortingquestion[0])
    
    choice = (input("").capitalize())

    if choice == sortingquestion[1]:
        HogwartsHouse.append(sortingquestion[3])
        line = sorting_hat_file.readline()
        sortingquestion = line.split(",")
    
    elif choice == sortingquestion[2]:
        HogwartsHouse.append(sortingquestion[4])
        line = sorting_hat_file.readline()
        sortingquestion = line.split(",")
   
    else:
        choice = input(f'Not a valid choice...\n')

print(HogwartsHouse)

# tallies the number of houses chosen in questions
Gryffindor = HogwartsHouse.count("G")
Slytherin = HogwartsHouse.count("S")
Hufflepuff = HogwartsHouse.count("H")
Ravenclaw = HogwartsHouse.count("R")

list_sorted_houses = sorted([(Gryffindor, "G"), (Slytherin, "S"), (Hufflepuff, "H"), (Ravenclaw, "R")], key = None, reverse = True)

print(list_sorted_houses[0])

if "G" in list_sorted_houses[0]:
    print(f'Congratulations, you have been sorted into Gryffindor!')

if "S" in list_sorted_houses[0]:
    print(f'Congratulations, you have been sorted into Slytherin!')

if "H" in list_sorted_houses[0]:
    print(f'Congratulations, you have been sorted into Hufflepuff!')

if "R" in list_sorted_houses[0]:
    print(f'Congratulations, you have been sorted into Ravenclaw!')


