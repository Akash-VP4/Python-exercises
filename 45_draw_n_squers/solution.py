def draw_n_squares(n):
    top = "+---"
    side = "|   "

    squares = ""
    for i in range(n):
        #   print(top*5,end = "+\n")
        squares += top * n + "+\n"
        #   print(side*5,end = "|\n")
        squares += side * n + "|\n"
    # print(top*5,end = "+\n")
    squares += top * n + "+"

    return squares
