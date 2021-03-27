# coding=utf-8
class Restarurant:
    """
        餐馆
    """
    def __init__(self, restarurant_name, cuisine_type):
        self.restarurnat_name = restarurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restarurant(self):
        print("restarurant-name is : {}, cuisine-type is : {}".format(
            self.restarurnat_name, self.cuisine_type
        ))

    def open_restarurant(self):
        print("{} is open!".format(self.restarurnat_name))

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, numbers):
        self.number_served += numbers


class IcecreamStand(Restarurant):
    """
        冰淇淋继承餐馆
    """
    def __init__(self, flavors):
        self.flavors = flavors

    def get_ice_flavors(self):
        for flavor in self.flavors:
            print(flavor)



if __name__ == '__main__':
    # res = Restarurant('深夜豆浆店', '夜宵')
    # print res.restarurnat_name, res.cuisine_type
    # print res.number_served
    # # res.number_served = 10
    #
    # res.set_number_served(20)
    # res.increment_number_served(50)
    # print res.number_served


    # res.describe_restarurant()
    # res.open_restarurant()
    #
    # res2 = Restarurant('桂林米粉', '粉铺')
    # res2.describe_restarurant()
    #
    # res3 = Restarurant('大鸽饭', '湘菜')
    # res3.describe_restarurant()


    ice = IcecreamStand(['ICE', '草莓'])
    ice.get_ice_flavors()