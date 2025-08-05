def main():
    a = 5

    # Use if else to check if a is positive or negative
    print("===================IF-ELSE=============================")
    if a > 0:
        print("a is a positive number!")
    elif a == 0:
        print("a is zero!")
    else:
        print("a is a negative number!")

    # Use for-loop to print all the numbers from 0 to a-1
    print("===================FOR-LOOP=============================")
    for i in range(a):
        print(i)

    # Another way to loop is via while
    print("===================WHILE-LOOP=============================")
    while a > 0:
        a = a - 1
        print(a)


# This is only executed when invoking this script
if __name__ == "__main__":
    main()
