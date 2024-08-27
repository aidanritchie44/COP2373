#This assignment simulates a Magic 8 Ball, which is a fortune telling toy
# that displays a random response to a yes or no question.
#The first part of the program should create a file called 8ball_responses.txt
# with 12 different phrases in the file
#The second part of the program should read the responses from the file into a list.
# It should then prompt the user to ask a yes/no type question, then randomly
# display one of the responses. The program should repeat until the user is ready to quit.

#create a function that creates a txt file with the desired phrases listed

def txt():

#use 'phrases' as variable

    phrases = ['Yes, of course!',
            'Without a doubt, yes!',
            'You can count on it.',
            'For Sure!',
            'Ask me later!',
            'Im not sure.',
            'I cant tell you right now.',
            'Ill tell you after my nap.',
            'No way!',
            'I dont think so.',
            'Without a doubt, no.',
            'The answer is clearly NO!']
#open file and prepare it so that code can write with it
    with open('8ball_responses.txt', 'w') as file:

        for phrase in phrases:
            file.write(phrase + '\n')
#call function

txt()

#next, use import random for generating random words
#then create another function that asks for user input and outputs random answers

import random
def main():
#open txt file and read the responses
    infile = open('8ball_responses.txt', 'r')
    response_list = infile.readlines()
    for index in range(len(response_list)):
        response_list[index] = response_list[index].rstrip('\n')
#allow user to ask a question, and code so that one of the phrases is used as the output
#incorporate while loop so if user would like to ask another question, they can.
#if not, program ends.
    again = 'y'
    while again == 'y' or again == 'Y':
        qst =input('Ask me a yes or no question and get your answer:')
        print(response_list[random.randint(0, len(response_list) -1)])

        print('Would you like to ask me another question?')
        again = input('[Y/N] to continue: ')
#call function
main()









