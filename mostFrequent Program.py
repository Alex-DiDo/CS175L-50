'''
Alexander DiDomenico
CS175L-50
#mostFrequent
'''

def mostFrequent(List):
    count = 0
    num = List [0]

    for n in List:
        frequency = List.count(n)
        if (frequency> count):
            count = frequency
            num = n

    return num 

count_alphabet= {
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5',
    'f':'6',
    'g':'7',
    'h':'8',
    'i':'9',
    'j':'10',
    'k':'11',
    'l':'12',
    'm':'13',
    'n':'14',
    'o':'15',
    'p':'16',
    'q':'17',
    'r':'18',
    's':'19',
    't':'20',
    'u':'21',
    'v':'22',
    'w':'23',
    'x':'24',
    'y':'25',
    'z':'26'
}
'''
alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

for number in alphabet:
    alphabet = number
'''
List = input('Enter a String: ')
print('These are the counts for each letter of the alphabet: ',count_alphabet)
print('The character that appears most frequently in the string is ',mostFrequent(List), '.')
