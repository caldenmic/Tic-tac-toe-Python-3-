import sys

def gameBoard():
    print('\n')
    print("_{}_\t_{}_\t_{}_\n".format(data_store[0][0], data_store[0][1], data_store[0][2]))
    print("_{}_\t_{}_\t_{}_\n".format(data_store[1][0], data_store[1][1], data_store[1][2]))
    print("_{}_\t_{}_\t_{}_\n".format(data_store[2][0], data_store[2][1], data_store[2][2]))
    print('\n')

def instructions():
    print('1.The player must enter the numbers from as rows and columns\n')

def Game():
    count = 0
    while(1):
        instruction_flag = str(input('Do you want to know the instructions y/n : '))
        if(instruction_flag == 'y'):
            instructions()
        if(instruction_flag=='y' or instruction_flag=='n'):
            break
    print('\n')
    Player1 = str(input('Enter player 1 name : '))
    print('{} will be using X'.format(Player1))
    Player2 = str(input('Enter player 2 name : '))
    print('{} will be using 0'.format(Player2))
    gameBoard()
    print('{} starts first'.format(Player1))
    for i in range(1, 11):
        if(i%2  == 0):
            Draw(2, count, Player1, Player2)
            count += 1
        else:
            Draw(1, count, Player1, Player2)
            count += 1

def Draw(player, count, Player1, Player2):
    print('\n')
    while(1):
        if(count >= 5):
            Check(Player1, Player2)  
        row = int(input('Enter row : '))
        col = int(input('Enter column : '))
        if(row >=3 or col >=3 or row < 0 or col < 0):
            print('\n')
            print('Invalid row and column value')
            print('\n')
            continue
        if((data_store[row][col] == '') and (player == 1)):
            data_store[row][col] = 'X'
        if((data_store[row][col] == '') and (player == 2)):
            data_store[row][col] = '0'
        print('\n')
        gameBoard()
        break

def Check(Player1, Player2):
    if(data_store[0][0] == data_store[0][1] == data_store[0][2] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[0][0] == data_store[0][1] == data_store[0][2] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[1][0] == data_store[1][1] == data_store[1][2] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[1][0] == data_store[1][1] == data_store[1][2] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[2][0] == data_store[2][1] == data_store[2][2] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[2][0] == data_store[2][1] == data_store[2][2] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[0][0] == data_store[1][0] == data_store[2][0] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[0][0] == data_store[1][0] == data_store[2][0] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[0][1] == data_store[1][1] == data_store[2][1] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[0][1] == data_store[1][1] == data_store[2][1] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[0][2] == data_store[1][2] == data_store[2][2] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[0][2] == data_store[1][2] == data_store[2][2] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[0][0] == data_store[1][1] == data_store[2][2] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[0][0] == data_store[1][1] == data_store[2][2] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()
    if(data_store[0][2] == data_store[1][1] == data_store[2][0] == 'X'):
        print('{} has won'.format(Player1))
        sys.exit()
    if(data_store[0][2] == data_store[1][1] == data_store[2][0] == '0'):
        print('{} has won'.format(Player2))
        sys.exit()

if __name__ == '__main__':
    data_store = [['']*3 for _ in range(3)]
    Game()

