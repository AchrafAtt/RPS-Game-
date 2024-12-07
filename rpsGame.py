import random , sys

print('ROCK, PAPER, SISSORS')

#TRACK THE RESULT
wins=0
losses=0
ties=0

while True: #main game
    print('%s Wins,%s Losses,%s Ties' %(wins,losses,ties))
    while True: #loop game 
        print('Entre your move: (r)Rock (p)Paper (s)SISSORS')
        movePlayer=input()
        if movePlayer=='q':
            sys.exit()
        if movePlayer =='r' or movePlayer=='r' or movePlayer=='p' :
            break #out of game loop
        print('Type one of r, p, s or q.')

    #Display what player chose:
    if movePlayer == 'r':
        print('Rock versus...')
    elif movePlayer =='p':
        print('Paper versus ....')
    elif movePlayer == 's':
        print('SISSORS verus ....')

    #display random chose computer
    randomNumber = random.randint(1,3)
    if randomNumber == 1 :
        computerMove= 'r'
        print('Rock')
    elif randomNumber ==2 :
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove= 's'
        print('SISSORS')

#display and record the  win/loss/tie

    if movePlayer == computerMove:
        print('It is tie !')
        ties +=1
    elif movePlayer == 'r' and computerMove == 's':
        print('you win !')
        wins+=1
    elif movePlayer == 'p' and computerMove =='r':
        print('you win !')
        wins+=1
    elif movePlayer == 's' and computerMove =='p':
        print('you win!')
        wins+=1

    elif movePlayer == 's' and computerMove == 'r':
        print('you losses !')
        losses+=1
    elif movePlayer == 'r' and computerMove =='p':
        print('you losses !')
        losses+=1
    elif movePlayer == 'p' and computerMove =='s':
        print('you losses!')
        losses+=1
    
    


