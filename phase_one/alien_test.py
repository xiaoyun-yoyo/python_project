# coding=utf-8
if __name__ == '__main__':
    #列表存在字典
    # aliens_list = []
    # for alien in range(1, 31):
    #     aliens_list.append({'color': 'green', 'points': 5, 'speed': 'slow'})
    # for alien in aliens_list[0:3]:
    #     if alien['color'] == 'green':
    #         alien['color'] = 'yellow'
    #         alien['points'] = 10
    #         alien['speed'] = 'medium'
    # for alien in aliens_list:
    #     print alien


    #字典存储列表
    # pizza = {
    #     'crust': 'thick',
    #     'toppings': ['mushrooms','extra cheese']
    # }
    # print "you ordered a {} pizza! with the" \
    #       "following toppings:".format(pizza['crust'])
    # for toppings in pizza['toppings']:
    #     print "\t"+toppings

    #在字典中存储字典
    users = {
        'aeinstein': {
            'first': 'aibert',
            'last': 'einstein',
            'location': 'princeton'
        },

        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        }
    }
    for username, userinfo in users.items():
        print("username {}".format(username))
        fullname = userinfo['first']+userinfo['last']
        location = userinfo['location']
        print("fullname: {} , location is : {}".format(fullname, location))