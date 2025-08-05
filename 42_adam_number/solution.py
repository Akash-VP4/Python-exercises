def check_adam_number(num):

    numString = str(num)
    num_reverse_square = str(int(numString[::-1]) * int(numString[::-1]))[::-1]
    num_square_reverse = str(int(str(num * num)))

    # print(num_reverse_square,num_square_reverse)
    # print(num_square_reverse)

    """Check if num is an Adam number"""
    return num_reverse_square == num_square_reverse
