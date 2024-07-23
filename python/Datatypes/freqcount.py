def count_num(lst, number):
    count = 0
    for i in lst:  # for i in  []
        if i == number:
            count += 1
    return count


def main():
    # dynamic input
    print('Enter the size of the list')
    size = int(input())
    data_input = []
    print('Enter the values : ')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User List : ', data_input)
    searchNum = int(input('Enter element to be checked list : '))
    print(searchNum, "is repeating ", count_num(data_input, searchNum))


if __name__ == "__main__":
    main()
