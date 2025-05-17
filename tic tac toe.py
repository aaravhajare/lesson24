board = {"9" : " ", "8" : " " , "7" : " " , "6" : " " , "5" : " " , "4" : " " , "3" : " " ,  "2" : " " , "1" : " " }  

board_keys = []

for key in board:
    board_keys.append(key)

def print_board(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])   
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])


def game():

    turn = "X"
    count = 0

    for i in range(10):
        print_board(board)

        print("turn for " , turn , "enter a num betwwween 1-9")
        move = input()

        if board[move] == " " : 
            board[move] = turn
            count += 1
        else:
            print("sorry the place is aldready filled")
            continue

        if count >= 5:
        
            if board["7"] == board["8"] == board["9"] != " ":
                print_board(board)
                print(turn , "wins")
                break

            elif board["4"] == board["5"] == board["6"] != " ":
               print_board(board)
               print(turn , "wins")
               break

            elif board["1"] == board["2"] == board["3"] != " ":
               print_board(board)
               print(turn , "wins")
               break

            elif board["7"] == board["4"] == board["1"] != " ":
               print_board(board)
               print(turn , "wins")
               break

            elif board["8"] == board["5"] == board["2"] != " ":
               print_board(board)
               print(turn , "wins")
               break

            elif board["9"] == board["6"] == board["3"] != " ":
               print_board(board)
               print(turn , "wins")
               break

            elif board["7"] == board["5"] == board["3"] != " ":
               print_board(board)
               print(turn , "wins")
               break

            elif board["9"] == board["5"] == board["1"] != " ":
               print_board(board)
               print(turn , "wins")
               break


        if turn == "X":
            turn = "O"
        else:
            turn = "X"

        if count == 9:
            print("it a tie")
            
            restart = input("do you want to restart the game? (yes/no)")
            if restart == "yes":
                for i in board_keys:
                    board[i] = " "
                game()

            else:
                print("thanks for playing")
                break

if __name__ == "__main__":
    game()
 