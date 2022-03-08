'''
Alexander DiDomenico
2/16/22
Resturant V2
'''

def callanswer(cancel):
    answer=input('Is anyone in your party{cancel}?')
    if answer.lower()=='yes':
        return Yes
    else:
        return No

vegetarian=input('Is anyone in your party a vegatrian? ')
vegan=input('Is anyone in your party a vegan? ')
gluten_free=input('Is anyone in your party gluten free? ')
print('Here are your restaurant choices:')
if vegatarian=='yes' and vegan=='yes' and gluten_free=='yes':
    print('Corner Cafe')
    print('The Chefs Kitchen')
if vegatarian=='no' and vegan=='yes' and gluten_free=='yes':
    print('Corner Cafe')
    print('The Chefs Kitchen')
if vegatarian=='yes' and vegan=='no' and gluten_free=='yes':
    print('Corner Cafe')
    print('Main Street Pizza Company')
    print('The Chefs Kitchen')
if vegatarian=='yes' and vegan=='yes' and gluten_free=='no':
    print('The Chefs Kitchen')
    print('Corner Cafe')
if vegatarian=='no' and vegan=='no' and gluten_free=='yes':
    print('Corner Cafe')
    print('Main Street Pizza Company')
    print('The Chefs Kitchen')
if vegatarian=='yes' and vegan=='no' and gluten_free=='no':
    print('The Chefs Kitchen')
    print('Corner Cafe')
    print('Main Street Pizza Company')
    print('Mamas Fins Italian')
if vegatarian=='no' and vegan=='yes' and gluten_free=='no':
    print('Corner Cafe')
    print('The Chefs Kitchen')
else:
    print('Corner Cafe')
    print('Joes Gourmet Burgers')
    print('Mamas Fine Italian')
    print('Main Street Pizza Company')
    print('The Chefs Kitchen')
answer = input('Would you like to search again?')
if answer.lower()=='no':
    print('Goodbye!')
else:
    print('Search again: ')
