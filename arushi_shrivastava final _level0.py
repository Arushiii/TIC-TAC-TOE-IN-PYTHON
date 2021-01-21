#!/usr/bin/env python
# coding: utf-8

# In[4]:


#first I have imported these libraries:
import numpy as np
import random


#then I asked the user for the grid dimenstions: m*n and the k value:  
row= int(input('Please enter the no. of rows you want: '))
print()
col= int(input('Please enter the no. of columns you want: '))
print()
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
#print('This is how the board looks like!! Enjoy!! ')

#here I asked the user to give input where they want to put x in the matrix
def insertBoard():
    print()
    e= int(input('Hi, in which row you want to place the x:  '))
    print()
    f = int(input('Hi, in which column you want to place the x:  '))
    board[e][f] = 'x'
    
#here i find all the available positions in the matrix
def available_moves(board):
    m, n = board.shape
    am = [] # to accumulate available moves as tuples
    for i in range(m):
        for j in range(n):
            if board[i,j] == '_': am.append((i,j))
    return am
#here the computer plays his chance after the user 
def random_place(board, player):
    player= 'o'
    selection = available_moves(board)
    current_loc = random.choice(selection) 
    board[current_loc] = player 
    return(board)

#now this is the main function to call all the other functions
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
#this is the recursive function that I have genrated for taking the input from the user and the computer
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
        random_place(board,'o')
        print_board(board)
        tfmatrix(k,board)
        sdf()
    
    else:
        print()
        print('bye!')
sdf()


# In[3]:


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





# In[ ]:




