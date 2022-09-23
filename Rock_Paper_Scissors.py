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


import random
print("Welcome to Rock, Paper, Scissors!!!")
ourmove = int(input("Choose 0 for rock, 1 for paper, 2 for scissors "))

random.seed(ourmove)
computermove = random.randrange(0,2)

combined = [rock, paper, scissors]

player = combined[ourmove]
computer = combined[computermove]

if ourmove==0 and computermove ==1:
	print("You chose:")	
	print(rock)
	print("Computer chose:")
	print(paper)
	print("Paper covers rock! You lose!!")

if ourmove==1 and computermove ==2:
	print("You chose:")	
	print(paper)
	print("Computer chose:")
	print(scissors)
	print("Scissors cuts paper! You lost!!")

if ourmove==2 and computermove ==0:
	print("You chose:")	
	print(scissors)
	print("Computer chose:")
	print(rock)
	print("Rocks breaks scissors! You lose!!")

if ourmove==0 and computermove ==2:
	print("You chose:")	
	print(rock)
	print("Computer chose:")
	print(scissors)
	print("Rocks breaks scissors! You win!!")

if ourmove==1 and computermove ==0:
	print("You chose:")	
	print(paper)
	print("Computer chose:")
	print(rock)
	print("Paper covers rock! You win!!")

if ourmove==2 and computermove ==1:
	print("You chose:")	
	print(scissors)
	print("Computer chose:")
	print(paper)
	print("Scissors cuts paper! You win!!")

elif ourmove == computermove:

	print("You chose:")	
	print(combined[ourmove])
	print("Computer chose:")
	print(combined[computermove])

	print("Its a draw!!")
