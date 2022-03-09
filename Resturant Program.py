'''
Alexander DiDomenico
2/9/22
Resturant Program
'''
#Input
keep_going = True
while keep_going == True:

    Personal_Input = ''
    vegetarian = False
    vegan = False
    gluten_free = False

    #Ask User for their choice

    #Vegetarian
    vegetarian = input('Is anyone is your party a vegetarian? ')
    if vegetarian == 'yes' or vegetarian == 'no':
        if vegetarian == 'yes':
            vegetarian = True
        else:
            vegetarian = False

    #Vegan
    vegan = input('Is anyone in your party a vegan? ')
    if vegan == 'yes' or vegan == 'no':
        if vegan == 'yes':
            vegan = True
        else:
            vegan = False

    #Gluten_free
    gluten_free = input('Is anyone in your party gluten free? ')
    if gluten_free == 'yes' or gluten_free == 'no':
        if gluten_free == 'yes':
            gluten_free = True
        else:
            gluten_free = False

        #Resturants
        Personal_Input = 'Here are your resturant choices: '
        if vegetarian == True:
             if vegan == True:
                 if gluten_free == True or gluten_free == False:
                     Personal_Input += 'Main Street Cafe' + \
                                       'The Chefs Kitchen'
             else:
                 if gluten_free == True:
                     Personal_Input += 'Main Street Pizza Company' + \
                                      'The Chefs Kitchen' + \
                                      'Corner Cafe'
                 else:
                     Personal_Input += 'Corner Cafe' + \
                                      'Main Street Pizza Company' + \
                                      'The Chefs Kitchen' + \
                                      'Mamas Fine Italian'
        if vegan == True:
            if gluten_free == True or gluten_free == False:
                Personal_Input += 'Corner Cafe' + \
                                 'The Chefs Kitchen
            if gluten_free == True:
                Personal_Input += 'Corner Cafe' + \
                                 'Main Street Pizza Company' + \
                                 'The Chefs Kitchen'
            else:
                Personal_Input += 'The Chefs Kitchen' + \
                                  'Joes Gourmet Burgers' + \
                                  'Main Street Pizza Company' + \
                                  'Mamas Fine Italian' + \
                                  'The Corner Cafe'
    print(Personal_Input)
    keep_going_switch=input('Do you want to keep going?')
    if keep_going_switch == 'no':
        keep_going = False 
