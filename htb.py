import random

#conversion table
table = [ 
    ['0' , '0000'],
    ['1' , '0001'],
    ['2' , '0010'],
    ['3' , '0011'],
    ['4' , '0100'],
    ['5' , '0101'],
    ['6' , '0110'],
    ['7' , '0111'],
    ['8' , '1000'],
    ['9' , '1001'],
    ['A' , '1010'],
    ['B' , '1011'],
    ['C' , '1100'],
    ['D' , '1101'],
    ['E' , '1110'],
    ['F' , '1111'],
]

#exercise generator
def get_hex():
    pair = table[round(random.random()*len(table)-1)]
    if(round(random.random())):
        given    = pair[1]
        solution = pair[0]
        target   = "hexidecimal"
    else:
        given    = pair[0]
        solution = pair[1]
        target   = "binairy"
    print("Convert this number to "+target+": "+ given)
    return solution

def create_problem():
    question = get_hex()
    answer = input("Answer: ")

    if(question==answer):
        print("Correct!")
        return 1
    else:
        print("Wrong! The answer was: "+question)
        return 0

running = True

#run the program
while(running):
    score = 0
    for i in range(0 ,5):
        score += create_problem()
    print("You've got "+str(score)+" out of 5 correct!")
    cont = input('Try again? y/n: ')
    if(cont == 'n'):
        running=False

print('Shutting down...')
