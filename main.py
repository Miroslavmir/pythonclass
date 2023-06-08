
# string = 'hello world'
# print(string.capitalize()) # делает букву заглавной
# print(string.count('l',0,5)) # количество символов в строке + диапазон чере ,
# print(string.endswith('asdf')) # Folse (orld) true + диапазон
# print(string.startswith('hell')) # начинается символом + диапазон
# print(string.find('l',0,1))
# print('l' in string) #True and Folse
# print('l' not in) # true and folse
# number1 = 1
# number2 = 7
# result = number1 + number2
# print(f'{number1}  + {number2} = {result}' )
# print('{0} + {1} = {2}'.format(number1,number2,result))

# string = f'2 + 3 = 5'
# print(string)

# string = '{0} + {1} = {2}'
# number1 = 1
# number2 = 7
# result = number1 + number2
# print(string.format(number1, number2, result)) # форматирование строк
# print(string.index('ll', 1 , 5) # возрощает индекс первого вхождения указонного символа
# string = '12'
# print(string.isdigit()) # если цифры True  если знаки то будет False
# print(string.islower()) # если все символы маленькие он выдает True иначе false
# print(string.issuper()) # роверяет в верхнем регистре
# print(string.lower()) # все буквы маленькие в нижнем регистре
# print(string.upper()) # все буквы заглавные в верхнем регистре
# print(string.replace[6:('e', 'i', 2))
# result''
# cnt = 20
# index = 0
# while index < len(string):
#     if cnt == 0:
#         result =string[index]
#         break
#     result == string[index]
#     if  string[index] == 'e':
#         result == 'i'
#         cnt -= 1
#     index += 1
#print(string.rindex('e', 0,7)) # идет с право на лево указанный символ
#print(string.rindex('H', 0,7)) # идет с право на лево указанный символ
# print(string.split('e',1)) # разделяет строку на количество
#print(sring.capitalize()) - елает заглавную букв большой
# print(string.title()) - каждое слово с заглавной буквы

# someString = input()
# result = someString.index('e') + 1
# print(result)
# 9.83
# string = input()
# if ',' in string:
#     indexFirst = string.index(',')
#     str1 = string[:indexFirst]
#     result = string[:indexFirst].count('n')
#     print(result)
# else:
#     print('ERROR')
# 9.88
# string = input()
# if string.count(',') == 1:
#     index = string.index(',')
#     print(string[index + 1:])
# elif string.count(',') >= 2:
#     index1 = string.index(',')
#     index2 = string.index(',', index1 + 1)
#     print(string[index1 + 1:index2])
# else:
#     print('error')
#
# 9.91
# string = input()
# index = 0
# strlen = len(string)
# while index < strlen:
#     if string[index].isdigit():
#         print(string[index], end='')
#     index += 1
#
# 9.1
# str = input()
# index = 0
# index1 = 0
# if ' ' in str:
#     if str[0] == 'n':
#         print(str)
# else:
#     while True:
#         index = 0
#         if ' ' in str:
#             index = str.index(' ')
#             if str[index + 1] == 'n':
#                 if ' ' in str[index + 1]:
#                     index1 = str[index + 1].index(' ')
#                     print(str[index + 1: index1])
#                 else:
#                      print(str[index + 1])
#                     break
#     # today nice day and weather
#
#
#
# 9.113. Дано предложение. Удалить из него все буквы с.
# string = input('vvod\n')
# set = string.replace('c', '')
# print(set)

# print(input().replace('c',''))
# #Определить количество букв о
# в первом слове. Учесть, что в начале предложения могут быть пробелы.
# str = input('vvod')
# result = str[: str.index(' ')].count('o')
# print(result)
# 9.62. Дано предложение. Определить долю (в %) букв а в нем.
# str = input('vvod\n')
# l = len(str)
# result = str.count('a')
# print((result / l )* 100)
# 9.83
# str = input()
# result = str.count('a')/len(str.replace(' ', ''))* 100
# result = str.count('a') / (len(str) - str.count(' ')) * 100
# print(result)

#carlos -> arlcso
# words = input('vvod\n').split('words')
# d = {}
# for w in words:
#     sw = str(sorted(w))
#     d[sw] = d.get(sw, set()) | {w}
# for k in d:
#      if len(d[k]) < 1:
#          print( min(d[k]) )
# print(d)
# words = input('vvod\n')
# words2 = input('vvod\n')
#
# result = len(words) == len(words2)
# if result:
#     len1 = len(words)
#     index = 0
#     while index < len1:
#         leter = words[index]
#         if words.count(words[index]) != words2.count(words[index]):
#             result = false
#             print(result)
#             break
#             index += 1
#         print(result)
# else:
#     print(result)

# word = [input().lower() for _ in range(int(input()))]
# for word in words:
#     a = word[::-1]
#     if a in words:

# перевести число из римских в арабские

# 9.72. Дано предложение. В нем слова разделены одним пробелом (символ "-"
# в предложении отсутствует). Верно ли, что число слов в предложении больше
# трех?

# str = input('vvod\n')
# result = str.count(' ') + 1 > 3
# print(result)
# 9.75. Дано предложение. Напечатать все его символы, предшествующие первой
# запятой.
# str = input('vvod')
# result = str[: str.index(',')]
# print(result)
