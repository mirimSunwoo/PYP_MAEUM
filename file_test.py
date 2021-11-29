check = input()
s_list = ['1', '2', '3']

if check == s_list[0]:
    file = open('미림마이스터고.txt', 'r', encoding="UTF-8")
    lines = file.readlines()
    for line in lines:
        lis = int(line)
        m = lis + 1
        print(m)

        # lis = line.split(" ")
        # lis = list(map(int, lis))
        # print(type(lis))

        #m = int(lis)
        #print(m)
        #m += 1
    #print('미림마이스터고 도네: ', m)
    file.close()
    # print(num)
    #
    # file = open('미림마이스터고.txt', 'a')
    # dona_count = int(num) + 1
    # print(dona_count)
    # file.write(dona_count)
    # file.close()
    #-------------------------------------
    #     file = open('미림마이스터고.txt', 'a')

    #     file.write('미림 플러스1')
    #     file.close()

    #     file = open('미림마이스터고.txt', 'r')
    #     print(file.read())

# elif check == s_list[1]:
#     file = open('선린인터넷고.txt', 'a')
#     file.write('선린 플러스1')
#     file.close()
#
#     file = open('선린인터넷고.txt', 'r')
#     print(file.read())
#     file.close()
#
# elif check == s_list[2]:
#     file = open('디지털미디어고.txt', 'a')
#     file.write('디미 플러스1')
#     file.close()
#
#     file = open('디지털미디어고.txt', 'r')
#     print(file.read())
#
# else:
#     print('ㅇ')
