def draw_hashtag(input):
    number_columns = input
    number_lines = number_columns

    for i in range(number_columns):
        for j in range(number_lines):
            auxiliary_variable = (number_columns - 1) - i
            if j >= auxiliary_variable:
                print("#", end='')
            else:
                print(" ", end='')
        print()


if __name__ == "__main__":
    draw_hashtag(6)
