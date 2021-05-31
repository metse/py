computer_choice = 'scissors'

user_choice = input('Rock, paper or scissors?\n')

if computer_choice == user_choice:
  print('Tie!')
elif computer_choice == 'rock' and user_choice == 'scissors':
  print('Computer wins!')
elif computer_choice == 'scissors' and user_choice == 'paper':
  print ('Computer wins!')
elif computer_choice == 'paper' and user_choice == 'scissors':
  print('Computer wins!')
elif computer_choice == 'scissors' and user_choice == 'paper':
  print ('Computer wins!')
else:
  pass