import random as rn

random_number = rn.randint(1,100)

while True:
    user_input = int(input("Enter number : "))

    if user_input > random_number:
        print("Number is Greater try again")

    elif user_input < random_number:
        print("Numbert is Smaller try again ")

    else:
        print("Niceee Good Job")
        break
