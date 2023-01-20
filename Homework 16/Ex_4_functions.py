

import json

def add_dishes ():

    dish_list = []

    while True:
        dish = input('Type in the dish or type Stop')
        if dish.lower() == 'stop':
            break
        else:
            dish_list.append(dish)
    with open('json_list', 'w+') as f:
        try:
            data = json.load(f)
        except:
            data ={}

        data['my_list'] = dish_list

        json.dump(data,f)

def list_dishes():
    with open('json_list','r') as f:
        data = json.load(f)
    try:
        dish_list = data['dish_list']
        print('List of dishes')

        for dish in dish_list:
            print(dish)
    except KeyError:
        print('No dishes found in list')


def show_menu():
    option = input('Select 1 to add dishes to the list. n/ Select 2 to see the dish list' )

    if option == '1':
        add_dishes()
    elif option == '2':
        list_dishes()
    else:
        print('Invalid choice, try again')



show_menu()