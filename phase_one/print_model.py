# coding=utf-8
from random import randint, choice
def print_models(unprinted_desins, completed_designs):
    while unprinted_desins:
        current_design = unprinted_desins.pop()
        print("printing model: {}".format(current_design))
        completed_designs.append(current_design)


def show_completed_models(completed_models):
    print("the following models have been printed: ")
    for completed in completed_models:
        print(completed)


if __name__ == '__main__':
    # unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # #   [:]不会改变原来的列表
    # # print_models(unprinted_designs, completed_models)
    # print_models(unprinted_designs[:], completed_models)
    #
    # print("yuanlai: {}".format(unprinted_designs))
    # show_completed_models(completed_models)
    print(randint(1, 9))
    players = ['charles', 'martina', 'michael', 'florence']
    print(choice(players))