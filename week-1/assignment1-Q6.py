# Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)

def score(no_of_game, win_game, loss_game):
    tie = no_of_game - win_game
    win_point = win_game * 4
    tie_point = (no_of_game - win_game) * 2
    result = win_point + tie_point
    print(f"total number of tie is {tie} and total point is {result} ")


no_of_game = int(input("Enter "))
win_game = int(input("Enter "))
loss_game = int(input("Enter "))

score(no_of_game, win_game, loss_game)
