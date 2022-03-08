score1=int(input('What is your first test score? '))
score2=int(input('What is your second test score? '))
score3=int(input('What is your third test score? '))
score4=int(input('What is your fourth test score? '))
score5=int(input('What is your fifth test score? '))

def computeletterGrade(number):
    letterGrade=''
    if number >= 90:
        letterGrade = 'A'

    elif number >= 80 and number < 90:
        letterGrade = 'B'

    elif number >=70 and number <80:
        letterGrade = 'C'

    elif number >=60 and number <70:
        letterGrade = 'D'

    elif number <60:
        letterGrade = 'F'
    return letterGrade

def computeAverage():
    Average = (score1+score2+score3+score4+score5)/5
    return Average

print('Average: ',computeAverage())
print(computeletterGrade(computeAverage()))
print(computeletterGrade(score1))
print(computeletterGrade(score2))
print(computeletterGrade(score3))
print(computeletterGrade(score4))
print(computeletterGrade(score5))
