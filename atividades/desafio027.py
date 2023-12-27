from random import randint

number_random = randint(0, 5)

user_guess = int(input('Enter the your guess: '))

if user_guess == number_random:
    print('yes, you are congratulation')
elif user_guess > number_random:
    print('the number random is bigger than guess')
else:
    print('the number random is minor than guess')
