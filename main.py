def bubble_sort(user):
    for i in range(len(user)):  # looping 1st time in length of array
        for j in range(i + 1, len(user)):  # looping 2nd time in length
            # of array
            if user[j] < user[i]:  # checking if second element is larger
                # than 1st element
                user[j], user[i] = user[i], user[j]  # if larger then swaping
                # with it
    return user


def insertion_sort(user):
    for i in range(1, len(user)):  # looping in main starting with index
        # 1 as digit at index 0 will automatically compared with index 1
        key = user[i]  # variable key with user index at ith
        j = i - 1  # variable j as it need to compare the current digit with
        # the previous digit
        while (j >= 0) and (user[j] > key):  # looping with while as needed to
            # check
            # that j should be greater than 0 and user with index at j should
            # be greater than
            # key i.e. user with index i
            user[j + 1] = user[j]  # finally swaping the value of user with
            # index j + 1 with user index at j
            j = j - 1   # change the value of j with j - 1 as to get the new
            # value i.e. compared with other value
        user[j + 1] = key  # finally getting the new value by swaping the value
        # of user index at j + 1 with key i.e. user index at i
    return user


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def merge_sort(list):
    if len(list) < 2:
        return list

    middle = len(list) / 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    return merge(left, right)


def main():
    user_value = raw_input("Enter comma separated number(s): \n>>")
    while True:
        try:
            user_input = [float(i) for i in user_value.split(',')]
            # creating a list of string and converting to float
            break
        except (ValueError, TypeError):
            print "Please enter a valid number!!"
            user_value = raw_input(">>")
    # calling all functions here so that it will not ask again for
    # input for different sort
    print """Bubble Sort: {0}, \nInsertion Sort: {1}, \nMerge Sort {2}
    """.format(bubble_sort(user_input), insertion_sort(user_input),
               merge_sort(user_input))


main()
