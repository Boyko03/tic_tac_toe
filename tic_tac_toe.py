import sys
import time

board = """
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
"""
print(board)

a = board[17]; b = board[21]; c = board[25];\
    d = board[45]; e = board[49]; f = board[53];\
    x = board[73]; y = board[77]; z = board[81];

def other_number(player, number):
    number = input("Enter number (1-9)\n")
    if is_num(number) == None:
        while is_num(number) == None:
            number = input("Enter number (1-9)\n")
            is_num(number)
    else:
        number = int(number)
        board(player, number)

    
def board(player, number):
    global a, b, c, d, e, f, x, y, z;
    if number == 1:
        if a == " ":
            a = player
        else:
            other_number(player, number)
    elif number == 2:
        if b == " ":
            b = player
        else:
            other_number(player, number)
    elif number == 3:
        if c == " ":
            c = player
        else:
            other_number(player, number)
    elif number == 4:
        if d == " ":
            d = player
        else:
            other_number(player, number)
    elif number == 5:
        if e == " ":
            e = player
        else:
            other_number(player, number)
    elif number == 6:
        if f == " ":
            f = player
        else:
            other_number(player, number)
    elif number == 7:
        if x == " ":
            x = player
        else:
            other_number(player, number)
    elif number == 8:
        if y == " ":
            y = player
        else:
            other_number(player, number)
    elif number == 9:
        if z == " ":
            z = player
        else:
            other_number(player, number)
            
    board = """
+---+---+---+
| """ + a + """ | """ + b + """ | """ + c + """ |
+---+---+---+
| """ + d + """ | """ + e + """ | """ + f + """ |
+---+---+---+
| """ + x + """ | """ + y + """ | """ + z + """ |
+---+---+---+  
    """
    
    print(board)
    
    a = board[17]; b = board[21]; c = board[25];\
    d = board[45]; e = board[49]; f = board[53];\
    x = board[73]; y = board[77]; z = board[81];

    return a, b, c, d, e, f, x, y, z;

def is_num(text):
    try:
        return int(text)
    except ValueError:
        return None

    
def playerX():
    player = "X"
 
    num = input("Enter number (1-9)\n")
    
    if num == "quit" or num == "q":
        sys.exit("Error message")
        
    if is_num(num) == None:
        while is_num(num) == None:
            num = input("Enter number (1-9)\n")
            is_num(num)
    else:
        num = int(num)

    board(player, num)

    if (a == b and a == c and a == player) or (d == e and d == f and d == player) or \
       (x == y and x == z and x == player) or (a == d and d == x and a == player) or \
       (b == e and b == y and b == player) or (c == f and f == z and c == player) or \
       (a == e and e == z and a == player) or (c == e and c == x and c == player):
        print(player + " wins!")
        time.sleep(3)
        #########################
        sys.exit()
        #########################
    elif a != " " and b != " " and c != " " and d != " " and e != " " \
         and f != " " and x != " " and y != " " and z != " ":
        print("Tie!")
        time.sleep(3)
        #########################
        sys.exit()
        #########################

def playerY():
    player = "O"

    num = input("Enter number (1-9)\n")
    
    if num == "quit" or num == "q":
        sys.exit()
        
    if is_num(num) == None:
        while is_num(num) == None:
            num = input("Enter number (1-9)\n")
            is_num(num)
    else:
        num = int(num)

    board(player, num)

    if (a == b and a == c and a == player) or (d == e and d == f and d == player) or \
       (x == y and x == z and x == player) or (a == d and d == x and a == player) or \
       (b == e and b == y and b == player) or (c == f and f == z and c == player) or \
       (a == e and e == z and a == player) or (c == e and c == x and c == player):
        print(player + " wins!")
        time.sleep(3)
        #########################
        sys.exit()
        #########################
    elif a != " " and b != " " and c != " " and d != " " and e != " " \
         and f != " " and x != " " and y != " " and z != " ":
        print("Tie!")
        time.sleep(3)
        #########################
        sys.exit()
        #########################

m = 0

print("Enter 'quit' or 'q' to quit. ")
while m == 0:
    playerX()
    playerY()
