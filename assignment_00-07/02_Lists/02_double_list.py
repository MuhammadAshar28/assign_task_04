def main():

    numbers = [1, 2, 3, 4]
    print("Original List:", numbers)
    # Using a for loop to double each element in the list
    for i in range(len(numbers)):
        numbers[i] *= 2  
    print("Doubled List:", numbers)


if __name__ == '__main__':
    main()