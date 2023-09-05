import random


def hangman():
    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar\
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk\
lion lizard llama mole monkey moose mouse mule newt otter owl panda\
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep\
skunk sloth snake spider stork swan tiger toad trout turkey turtle\
weasel whale wolf wombat zebra'.split(' ')
    answer = random.choice(words)
    hangman_graphics = [r'''
   ________
 |
 |
 |
/ \ ''', r'''
   ________
 |      0
 |
 |
/ \ ''', r'''
   ________
 |      0
 |     /
 |
/ \ ''', r'''
   ________
 |      0
 |     /|
 |
/ \ ''', r'''
   ________
 |      0
 |     /|\ 
 |
/ \ ''', r'''   
   ________
 |      0
 |     /|\ 
 |     /   
/ \ ''', r'''
   ________
 |      0
 |     /|\ 
 |     / \  
/ \ ''']
    print(hangman_graphics[0])
    guessed_letters = ['_' for i in range(len(answer))]
    print(*guessed_letters)
    incorrect_letters = []
    counter = 0
    loop_counter = 0
    for i in range(30):
        loop_counter += 1
        inpt = input('\nYour guess:')
        if len(inpt) == 1:
            if inpt in answer:
                if inpt in guessed_letters:
                    print('\nYou already guessed that letter!')
                else:
                    for j in range(len(answer)):
                        if inpt == answer[j]:
                            guessed_letters[j] = inpt
                            print('\nWrong guesses: ')
                            print(*incorrect_letters)
                            print(hangman_graphics[counter])
                            print(*guessed_letters)
                            if '_' not in guessed_letters:
                                print('\nYou won! the word was: ' + answer)
                                if loop_counter == 1:
                                    print('It took you ' + str(loop_counter) + ' try')
                                else:
                                    print('It took you ' + str(loop_counter) + ' tries')
                                break
            if inpt not in answer:
                if inpt in incorrect_letters:
                    print('\nYou already guessed that letter!')
                else:
                    counter += 1
                    if counter > 5:
                        print(hangman_graphics[counter])
                        print('\nYou lost :( the word was: ' + answer)
                        break
                    else:
                        incorrect_letters.append(inpt)
                        print('\nWrong guesses: ')
                        print(*incorrect_letters)
                        print(hangman_graphics[counter])
                        print(*guessed_letters)
        else:
            if inpt == answer:
                print('\nYou won! the word was: ' + answer)
                if loop_counter == 1:
                    print('It took you ' + str(loop_counter) + ' try')
                else:
                    print('It took you ' + str(loop_counter) + ' tries')
                break
            else:
                counter += 1
                if counter > 5:
                    print(hangman_graphics[counter])
                    print('\nYou lost :( the word was: ' + answer)
                    break
                else:
                    incorrect_letters.append(inpt)
                    print('Wrong guesses: ')
                    print(*incorrect_letters)
                    print(hangman_graphics[counter])
                    print(*guessed_letters)


hangman()
