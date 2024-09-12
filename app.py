# write 'hello world' to the console
print('hello world')

# Create a game loop that runs until the user quits
running = True
while running:

    #Prompt user for rock, paper, or scissors
    user_input = input('Enter rock, paper, or scissors: ')

    # Make sure user input is valid
    if user_input not in ['rock', 'paper', 'scissors', 'q']:
        print('Invalid input. Please enter rock, paper, or scissors.')
        continue    
    
    # randomly choose rock, paper, or scissors
    import random
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print(f'The computer chose: {computer_choice}')

    # Check who won
    if user_input == computer_choice:
        print('It\'s a tie!')
    elif user_input == 'rock' and computer_choice == 'scissors':
        print('You win!')
    elif user_input == 'paper' and computer_choice == 'rock':
        print('You win!')
    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You win!')
    else:
        print('You lose!')

    # Check if the user wants to quit the game
    if user_input == 'q':
        running = False
    else:
        print(f'You entered: {user_input}')
        print('Type q to quit the game')
        

