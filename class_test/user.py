# coding=utf-8
from restarurant import Restarurant as res

class User:
    """"
        user类
    """

    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self, *infos):
        print(self.firstname, self.last_name)

        for info in infos:
            print(info)

    def greet_user(self):
        print("hi,how are you {}".format(self.last_name))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """
        admin
    """
    def __init__(self,first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()



class Privileges:
    """
        privileges
    """
    def __init__(self, privileges=['select', 'check', 'write']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)





if __name__ == '__main__':
    # user1 = User('bob', 'hankuke')
    # user2 = User('tom', 'mengqi')
    # user1.describe_user('china')
    # user1.greet_user()
    #
    # user2.describe_user()
    # user2.greet_user()
    #
    # user2.increment_login_attempts()
    # user2.increment_login_attempts()
    # print user2.login_attempts
    # user2.reset_login_attempts()
    # print user2.login_attempts

    # pri = ['select', 'check', 'write']
    # admin = Admin('bob', 'hankuke')
    # admin.privileges.show_privileges()
    r = res('mifen', 'youtiao')
    r.describe_restarurant()
    # Restarurant('mifen', 'youtiao').describe_restarurant()