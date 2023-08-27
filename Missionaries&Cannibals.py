boat_side = "Right"
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

print('\U0001f482',missionaries_on_left, "\U0001f479", cannibals_on_left,"|\U0001f30a"*4,"\U0001f6A2|","\U0001f482",missionaries_on_right, "\U0001f479",cannibals_on_right)

while True:
    missionaries = int(input("Enter number of missionaries or to end enter 10:"))
    if missionaries == 10:
        print("YOU QUIT, GAME OVER!")
        break
    cannibals = int(input("Enter number of cannibals:"))

    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:  # number of people on boat should not exceed 2
        print("Invalid move")
        continue

    if boat_side == "Right":
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
            print("Invalid move")

        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals

        missionaries_on_left += missionaries
        cannibals_on_left += cannibals

        print("\U0001f482", missionaries_on_left, "\U0001f479", cannibals_on_left, "|\U0001f6A2", "\U0001f30a|"*4, "\U0001f482", missionaries_on_right, "\U0001f479",cannibals_on_right)
        boat_side = 'Left'

    else:
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
            print("Invalid move")

        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals

        missionaries_on_right += missionaries
        cannibals_on_right += cannibals

        print("\U0001f482", missionaries_on_left, "\U0001f479", cannibals_on_left,"|\U0001f30a"*4,"\U0001f6A2|","\U0001f482",missionaries_on_right, "\U0001f479",cannibals_on_right)
        boat_side = 'Right'


        if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
            print('You Lose')
            break
        if (missionaries_on_left == 3 and cannibals_on_left == 3):
            print('You win')
            break

# '\U0001f482' - missionaries
# '\U0001f479' - cannibals
# '\U0001f30a' - waves
# 'U0001f6A2' - boat






