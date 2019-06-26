#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def start_game():
    print('Welcome to Tic Tac Toe')
    mylist=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    name1=input('Player1 - Enter your name     \n')
    name2=input('Player2 - Enter your name     \n')
    a=False
    while a==False:
        play1=input(f'{name1}, choose either X or O:')
        print(play1)
        if play1=='X' or play1=='O':
            if play1=='X':
                play2='O'
            elif play1=='O':
                play2='X'
            a=True
        else:
            a=False
    c=''
    if c!='Yes':
        while c!='Yes':
            c=input('Are you ready - Yes or No:  ')
        if c=='Yes':
            print('These are the various position numbers on the board \n')
            print('   |   |   \n 7 | 8 | 9 \n   |   |   \n--- --- ---\n')
            print('   |   |   \n 4 | 5 | 6 \n   |   |   \n--- --- ---\n')
            print('   |   |   \n 1 | 2 | 3 \n   |   |   \n')
    count=1
    while True:
        if count%2==1:
            num=int(input(f'{name1} : {play1} \nChoose your next position from (1-9):    '))
            if 0<num<10:
                if mylist[num]==' ':
                    count+=1
                    position(num,mylist,count,play1,play2)
            elif num=='':
                continue
                
           
                
        elif count%2==0:
            num=int(input(f'{name2} : {play2} \nChoose your next position from (1-9):    '))
            if 0<num<10:
                if mylist[num]==' ':
                    count+=1
                    position(num,mylist,count,play1,play2)
            
            


def position(num,mylist,count,play1,play2):
    if mylist[num]==' ':
        if count%2==0:
            mylist[num]=play1
            display_board(mylist)
        elif count%2==1:
            mylist[num]=play2
            display_board(mylist)
        return
    elif mylist[num]=='X' or mylist[num]=='O':
        print('Position already used. \n\n')
        count-=1
        display_board(mylist)
        return
   
            
            
def display_board(mylist):
    print(f'   |   |   \n {mylist[7]} | {mylist[8]} | {mylist[9]} \n   |   |   \n--- --- ---\n')
    print(f'   |   |   \n {mylist[4]} | {mylist[5]} | {mylist[6]} \n   |   |   \n--- --- ---\n')
    print(f'   |   |   \n {mylist[1]} | {mylist[2]} | {mylist[3]} \n   |   |   \n')   
    result(mylist)
    return 



def result(mylist):
    win_x=['X','X','X']
    win_o=['O','O','O']
    d1={'l1':mylist[1:4],'l2':mylist[4:7],'l3':mylist[7:10]}
    d2={'l1':mylist[1:8:3],'l2':mylist[2:9:3],'l3':mylist[3:10:3]}
    d3={'l1':mylist[1:10:4],'l2':mylist[3:8:2]}
    d={'k1':d1,'k2':d2,'k3':d3}
    e={'a':win_x,'b':win_o}

    
    if win_x in list(d['k1'].values()) or win_x in list(d['k2'].values()) or win_x in list(d['k3'].values()):
        print('X is the winner')
        replay()
    elif win_o in list(d['k1'].values()) or win_o in list(d['k2'].values()) or win_o in list(d['k3'].values()):
        print('O is the winner')
        replay()
            
    elif ' ' not in mylist:
        print('Match Draw')
        replay()
    else:
        return
    

def replay():
    request=input('Do you want to play again - Yes or No: ')
    if request=='Yes':
        print('\n'*100)
        start_game()
    elif request=='No':
        print('Thank you for playing Tic Tac Toe')
    else:
        replay()


start_game()


# In[ ]:




