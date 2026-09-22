def u():
    secret_word = 'hunter'.upper().lower().title()
    guess = '' 
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    while secret_word != guess and not(out_of_guesses) :
        if guess_count < guess_limit:
            guess = input('Enter secret word: ').upper().lower().title()
            guess_count += 1
        else:
            out_of_guesses = True
    if secret_word == guess:
        print('You Win!')
    else:
        print('Out of guesses, You Lose!')   
    if out_of_guesses:
        print("Try again next time")
    else: 
        print("Congratulations")       


def hi():
    
    Retry = 1
    Quit = 2
    Reveal_Secret_Word = 3
    print("Type 1 to retry")
    print("Type 2 to Quit")
    print("Type 3 to Reveal Secret Word")
    print('-------------------------------')
    Number = int(input('Enter: '))
    if Number == 1:
        u()
    elif Number == 2:
        print('Exit')    
    elif Number == 3:
        print('The Secret Word was "hunter"')
    else:
        print('Enter the Follwing Number')


secret_word = 'hunter'.upper().lower().title()
guess = '' 
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("The Secret Word")
print("Hint: starts from 'h' end with 'r' contains 6 letters")
while secret_word != guess and not(out_of_guesses) :
    if guess_count < guess_limit:
        guess = input('Enter secret word: ').upper().lower().title()
        guess_count += 1
    else:
        out_of_guesses = True

if secret_word == guess:
        print('You Win!')
else:
    print('Out of guesses, You Lose!')   
    
if out_of_guesses:
    print("Try again next time") 
    print('-------------------------------')
    hi()
else: 
    print("Congratulations")       
    




    
