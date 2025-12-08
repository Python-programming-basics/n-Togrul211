#1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee',
           7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))


#2
users = [
 {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
 {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
 {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
 {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
 {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
 {'name': 'John', 'phone': '233-421-32', 'email': ''},
 {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
 {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
 {'name': 'Robert', 'phone': '420-2011', 'email': ''},
 {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
 {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
 {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
 {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
 {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
 {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
 {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}
]

result = []
for u in users:
    if u['phone'][-1] == '8':
        result.append(u['name'])

result.sort()
print(" ".join(result))


#3
result = []
for u in users:
    if 'email' not in u or u['email'] == '':
        result.append(u['name'])

result.sort()
print(" ".join(result))


#4
num = input()
d = {'0':'zero','1':'one','2':'two','3':'three','4':'four',
     '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

res = []
for digit in num:
    res.append(d[digit])

print(" ".join(res))


#5
courses = {
 "CS101": (3004, "Хайнс", "8:00"),
 "CS102": (4501, "Альварадо", "9:00"),
 "CS103": (6755, "Рич", "10:00"),
 "NT110": (1244, "Берк", "11:00"),
 "CM241": (1411, "Ли", "13:00")
}

course = input()
info = courses[course]
print(course, ":", info[0], ",", info[1], ",", info[2])


#6
keys = {
 'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333',
 'g':'4','h':'44','i':'444','j':'5','k':'55','l':'555',
 'm':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777',
 't':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999',
 ' ':'0','1':'1','.' : '1',',' : '11','?':'111','!':'1111',':' : '11111'
}

text = input().lower()
output = ""

for ch in text:
    if ch in keys:
        output = output + keys[ch]

print(output)


#7
morse = {
 'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
 'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
 'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
 'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
 'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---',
 '3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
 '8':'---..','9':'----.'
}

text = input().upper()
result = []

for ch in text:
    if ch in morse:
        result.append(morse[ch])

print(" ".join(result))


#8
result = {}
for i in range(11, 16):
    result[i] = i * i


#9
dict1 = {'a':100,'z':333,'b':200,'c':300,'d':45,'m':230}
dict2 = {'a':300,'b':200,'d':400,'c':12,'z':666}

result = {}
for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    if key in result:
        result[key] = result[key] + dict2[key]
    else:
        result[key] = dict2[key]


#10
text = 'footballcyberpunkextraterritoriality'
result = {}

for ch in text:
    if ch in result:
        result[ch] = result[ch] + 1
    else:
        result[ch] = 1


#11
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley'
words = s.split()

count = {}
for w in words:
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1

mx = max(count.values())
res = []

for k in count:
    if count[k] == mx:
        res.append(k)

res.sort()
print(res[0])


#12
pets = [
 ('Hatiko', 'Parker', 'Wilson', 50),
 ('Rusty', 'Josh', 'King', 25),
 ('Balto', 'Josh', 'King', 25),
 ('Barry', 'Josh', 'King', 25)
]

result = {}

for dog, name, surname, age in pets:
    key = (name, surname, age)
    if key not in result:
        result[key] = []
    result[key].append(dog)


#13
text = input().lower()
for ch in ".,!?:;-":
    text = text.replace(ch, " ")

words = text.split()
count = {}

for w in words:
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1

mn = min(count.values())
res = []

for k in count:
    if count[k] == mn:
        res.append(k)

res.sort()
print(res[0])


#14
ids = input().split()
used = {}
result = []

for x in ids:
    if x not in used:
        used[x] = 0
        result.append(x)
    else:
        used[x] = used[x] + 1
        result.append(x + "_" + str(used[x]))

print(" ".join(result))
