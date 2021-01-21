#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import random


#then I asked the user for the grid dimenstions: m*n and the k value:  
row= int(input('Please enter the no. of rows you want: '))
print()
col= int(input('Please enter the no. of columns you want: '))
print()
print('k should not be smaller then row or column')
k= int(input('Please enter the value of k that you want to win: '))
print()
board = np.full((row,col), '_')

#then I have created the board on the basis of the numpy array based on user requirements
def print_board(board):
    m, n = board.shape   
    print(' ')
    for i in range(m):
        print (' ', end='')
        for j in range(n):
            print(board[i,j], end=' ')
        print(' ')
    print(' ')
    
def insertBoard():
    print()
    e= int(input('Hi, in which row you want to place the x:  '))
    print()
    f = int(input('Hi, in which column you want to place the x:  '))
    if board[e][f]=='_' and board[e][f]!='o' and board[e][f]!='x':
        board[e][f] = 'x'
    else:
        print('already occupied please enter new value')

def available_moves(board):
    m, n = board.shape
    am = [] # to accumulate available moves as tuples
    for i in range(m):
        for j in range(n):
            if board[i,j] == '_': am.append((i,j))
    return am
def random_place(board, player):
    player= 'o'
    selection = available_moves(board)
    current_loc = random.choice(selection) 
    board[current_loc] = player 
    return(board)
def main():
    print()
    print('Hi, Welcome to Tic Tac Toe!!  ')
    print()
    print('Your board looks like this, Have fun!!  ')
    print_board(board)
    print()
    print('This is your chance to play. Please enter the i, j:  ')
    insertBoard()
    print()
    print('Updated:  ')
    print_board(board)
    print()
    print('This is computer chance: ')
    random_place(board,'o')
    print_board(board)
main()

def sdf():
    print('do you want to continue')
    x= input('y or n: ')
    
    if x=='y' and len(available_moves(board))!=0:
        #board = np.full((row,col), '_')
        print('This is your chance to play. Please enter the i, j:  ')
        insertBoard()
        print()
        print('Updated:  ')
        print_board(board)
        print()
        print('This is computer chance: ')
        level0(board)
        print_board(board)
        tfmatrix(k,board)
        sdf()
                
    
    else: 
        print()
        print('bye!')
sdf()


# In[6]:


def level0(board):
    u = []
    find_o=  board=='o'
    yoyo= index_y,index_x = np.where(find_o == True)
    u.append(yoyo)
    f = find_o == True
    for i in u:
        
        a= i[-2]
        b= i[-1]
    
        one = []
        two = []
        for h in a:
            #print(h)
            one.append(h)
        print(one)
        for g in b:
            #print(g)
            two.append(g)
        print(two)
        zz= [one[-1]]
        xyzz = [two[-1]]
        z = np.array(zz)
        xyz = np.array(xyzz)

    try:
        if board[z,xyz]=='_' and board[z,xyz]!='x' and board[z,xyz]!='o':
            board[z,xyz]='o' 

        elif board[z,xyz-1]=='_' and board[z,xyz-1]!='x' and board[z,xyz-1]!='o':
            board[z,xyz-1]='o' 
        elif board[z+1,xyz-1]=='_'and board[z+1,xyz-1]!='x' and board[z+1,xyz-1]!='o':
            board[z+1,xyz-1]='o' 
        elif board[z-1,xyz]=='_'and board[z-1,xyz]!='x' and board[z-1,xyz]!='o':
            board[z-1,xyz]='o'
        elif board[z,xyz+1]=='_' and board[z,xyz+1]!='x' and board[z,xyz+1]!='o':
            board[z,xyz+1]='o'
        elif board[z+1,xyz]=='_' and board[z+1,xyz]!='x' and board[z+1,xyz]!='o':
            board[z+1,xyz]='o'       
        elif board[z+1,xyz+1]=='_' and board[z+1,xyz+1]!='x' and board[z+1,xyz+1]!='o':
            board[z+1,xyz+1]='o'
    
        elif board[z-1,xyz-1]=='_' and board[z-1,xyz-1]!='x' and board[z-1,xyz-1]!='o':
            board[z-1,xyz-1]='o'
        elif board[z-1,xyz+1]=='_' and board[z-1,xyz+1]!='x' and board[z-1,xyz+1]!='o':
            board[z-1,xyz+1]='o'
        elif board[z+1,xyz-1]=='_' and board[z+1,xyz-1]!='x' and board[z,xyz-1]!='o':
            board[z+1,xyz-1]='o'
    except:
        print('done')

    
    
    
level0(board) 


# In[9]:


def tfmatrix(k,board):
    y= []
    for i in range(k) :
        y.append(i)
    a=[]
    fo=[]
    for i in range(len(y)):
        n= 'x'
        g ='o'
        a.append(n)
        fo.append(g)
        mysearch = np.array(a)
        mysearch1=np.array(fo)
    #print(mysearch)
    #print(board==mysearch)
    
    win_r=np.all(board==mysearch,axis=1)   # when i check for rows
    win_r1=np.all(board==mysearch1,axis=1)
    #print(win_r)
    for i in win_r:
        #print(i)
        if i==False:
            print()
        else:
            print('x win')
            break
    for i in win_r1:
        #print(i)
        if i==False:
            print()
        else:
            print('o win')
            break

    
    
    win_c=np.all(board==mysearch,axis=0)
    win_c1=np.all(board==mysearch1,axis=0)
    #print(win_c)
    for i in win_c:
        #print(i)
        if i==False:
            print()
        else:
            #print('found')
            print('x win')
            break
    for i in win_c1:
        #print(i)
        if i==False:
            print()
        else:
            #print('found')
            print('o win')
            break

    d1=board.diagonal()
    d2=np.fliplr(board).diagonal()
    win_d1=np.all(d1==mysearch)
    win_d2=np.all(d2==mysearch)
    win_d11=np.all(d1==mysearch1)
    win_d21=np.all(d2==mysearch1)

    if win_d1==False:
        print()
    else:
        print('x win')
    if win_d2==False:
        print()
    else:
        print('x win')
        
    if win_d11==False:
        print()
    else:
        print('o win')
    if win_d21==False:
        print()
    else:
        print('o win')


tfmatrix(k,board)


# In[ ]:




