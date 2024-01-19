import random

number = []
number.append(random.randint(1, 9))
number.append(random.randint(1, 9))
number.append(random.randint(1, 9))
number.append(random.randint(1, 9))

print("****")

guess = None




while guess != number:
    print("guess the 4 digit number")
    temp = input()
    guess = []
    for x in temp:
        guess.append(int(x))
    
    for i in range(len(number)):
        
        print(number[i] == guess[i])
        print("----------------------------\n")
        if (guess[i] == number[i]): 
            print("number" + str(i + 1) + " is correct.""\n")
        else:
            for j in range(len(number)):
                if (i != j):
                    if (guess[i] == number[j]):
                        print("number" + str(i + 1) + " exist in another positon.""\n")
guess = number 
print("You win")
