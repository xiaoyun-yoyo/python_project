# coding=utf-8

if __name__ == '__main__':
    #打印1-20
    # for num in range(1, 21):
    #     print num


    # num_list = []
    # for i in range(1, 101):
    #     num_list.append(i)
    # print min(num_list)
    # print max(num_list)
    # print sum(num_list)

    # fruit_list = []
    # if fruit_list:
    #     print True
    # else:
    #     print False

    user_0 = {
        'user_name': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
        'test': 'fermi'
    }
    for key, value in user_0.items():
        print("key: {}".format(key))
        print("value: {}\n".format(value))
    print(user_0.items())

    for key in user_0.keys():
        print(key)
    print("\n")
    for value in user_0.values():
        print (value)
    print("\n")
    for value in set(user_0.values()):
        print(value)