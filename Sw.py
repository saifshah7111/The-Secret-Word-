secret_word = 'hunter'.upper().lower().title()
guess = '' 
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("The Secret Word")
print("Hint: starts from 'h'end with 'r' contains 6 letters")
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
    
