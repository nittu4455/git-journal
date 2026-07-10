import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice1 = int(input("Choose your option, 0 for rock, 1 for paper and 2 for scissors"))


Choice_list = [rock , paper, scissors]

A = Choice_list[choice1]
print(A)

random_gen = random.randint(0,2)

print("Computer Chose")

B = Choice_list[random_gen]
print(B)

if A == B:
    print("its a Draw")

elif (A == rock and B == scissors) or (A == scissors and B == paper) or (A == paper and B == rock) :
    print("You win")

else:
    print("you lose")


