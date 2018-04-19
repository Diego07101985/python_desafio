def print_numbers():

    for i in range(1, 101):
        if (i % 7 == 0) & (i % 3 == 0):
            print("Hello World")
        elif i % 3 == 0:
            print("Hello")
        elif i % 7 == 0:
            print("World")
        else:
            print(i)


if __name__ == "__main__":
    print_numbers()