def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers.")
    last_num = float(input("Enter num: "))
    curr_num = float(input("Enter num: "))
    sequence_length = 0
    while curr_num >= last_num:
        sequence_length += 1
        last_num = curr_num
        curr_num = float(input("Enter num: "))

    print("Thanks for playing!")
    print("Sequence length: " + str(sequence_length))

if __name__ == "__main__":
    main()