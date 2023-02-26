# lst = [11, 7 , 9 , 4, 13, 25, 14 , 8]

def largest(lst=None):
    temp = 0
    temp_1 = 0
    temp_2 = 0
    t = lst
    new_list = []
    n = len(lst)
    for c in t:
        for i in range(1, n):
                # print("The c test is",c[test])
                if (c)> temp:
                    temp = c

                    c = t[i]
                    print("The last value now is",c)
                    i = i + 1






                # t_max = c[i]
                # new_list = new_list.append(temp)
                # lst[0] = lst[i]
                # i = i + 1



                else:
                    c = temp_1
                    c = t[i]

                    print("The last value now is", c)
                # lst[0] = lst[i]
                # new_list = new_list.append(temp)
                    i = i + 1
        print("The highest number is ",temp)
        return (temp)
        exit
        # new_list = new_list.append(temp)
    exit()

def main():
    print("To find the largest number in a given list")

    lst = [11, 7, 9, 4, 13, 25, 14, 8]

    result = largest(lst)

    to_find = lst.index(result)
    print("To find", to_find)

    lst_1 = lst.pop(to_find)

    print("The list is ", lst)

    second_largest = largest(lst)
    to_find_2 = lst.index(second_largest)


    lst_2 = lst.pop(to_find_2)

    print("The list is ", lst)

    third_largest = largest(lst)


    print("The third largest number is ", third_largest)


main()
