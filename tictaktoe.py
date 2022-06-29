print('''
player1'll play with O.
player2'll play with X.
lets play... ''')#info about game.

def set(add):#set up off tic tak toe..
    for i in range(3):
        print(f'\t\t\t {add[3*i]} | {add[(3*i+1)]} | {add[3*i+2]}')
        if i<2:
            print("\t\t\t--------------")  

def game():

    p1 = input('player 1 enter your name>')  # users name
    p2 = input('player 2 enter your name>')

    adr = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

    set(adr)  # set the set up of tic tac toe

    for i in range(5):
        
        m2 = input(f'\n{p2} make your move>')

        while m2 not in adr:
            print('wrong address')
            set(adr)
            m2 = input(f'\n{p2} make your move>')
            
        adr[adr.index(m2)] = ' X'
            
        set(adr)

        check = [adr[0:3], adr[3:6], adr[6:], adr[0:7:3],
                 adr[1:8:3], adr[2::3], adr[0::4], adr[2:7:2]]

        # X wins
        if [' X',' X',' X'] in check:
            print(f'\n\a{p2} won:')
            r = input('''enter 'r' for play again..any other key for exit>''')
            if r=='r':
                game()
            break

        #tie
        if i == 4:
            print(f'\n\aTie ..')
            r = input('''enter 'r' for play again..any other key for exit>''')
            if r == 'r':
                game()
            break

        m1 = input(f'\n{p1} make your move>')
        while m1 not in adr:
            print('wrong address')
            set(adr)
            m1 = input(f'\n{p1} make your move>')

        adr[adr.index(m1)] = ' O'

        set(adr)

        check = [adr[0:3], adr[3:6], adr[6:], adr[0:7:3],
                 adr[1:8:3], adr[2::3], adr[0::4], adr[2:7:2]]

        # O wins
        if [' O',' O',' O'] in check:
            print(f"\n\a{p1} won:")
            r = input('''enter 'r' for play again..any other key for exit>''')
            if r == 'r':
                game()
            break

game()


