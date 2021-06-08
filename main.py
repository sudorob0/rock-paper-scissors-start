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
hands = [rock, paper, scissors]

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
#numPlayer = int(player)
if player > 2 or player < 0:
  print('Invalid number, try again')
print(hands[player])

computer = random.randint(0, 2)
print('Computer chose:')
print(hands[computer])

if player == 0 and computer == 2:
  print('You win')
elif player > computer:
  print('You win')
elif player == computer:
  print('Tie')
else:
  print('You lose')