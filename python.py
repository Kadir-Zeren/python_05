text = 'Clarusway'
print(text[0])

print(text[:5] + 'k' + text[-3:])

text='AaBbCc'
print(text.lower())

text = text.lower()
print(text)

var_str = 'In God we Trust'
print(var_str.lower())

cumle = 'In God We Trust'
print(cumle.lower())

print('t' in cumle)
print('R' in cumle)
print('trust' in cumle)
print('R' not in cumle)

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('http:'))

text = 'aabbcc'
print(text.startswith('a'))
print(text.startswith('aa'))
print(text.startswith('b',2))
print('abcdeabcde'.startswith('c',2,8))
print('****')
email = 'clarusway@clarusway.com is my e-mail address'
print(email.startswith("@",9))
print(email.endswith("-",10,32))

text='a b c d'
print(len(text))
email = 'clarusway@clarusway.com is my e-mail address'
print(email[10:32])
text = 'www.clarusway.com'
print(text.endswith('.co'))
print(text.startswith('w.'))
text = 'abcdef'
print(text.startswith('b',-5))

text = "asdasdas sad asdasd asdasd asd as d"
print('sayac',text.count(' ')+1)

text = 'abcabcabc'
print(text.find('ca'))
print(text.find('klm'))
print(text.rfind('a'))
print(text.index('ca'))
text = 'www.clarusway.com'
print(text.index('com'))
print(text.find('com'))

text = 'ClaRusWay'
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text.replace('W',"***").lower())
print(text.replace('w',"***").lower().upper())

sentece = 'I live and work in Virginia'
title_sentence = sentece.title()
print(title_sentence)

changed_sentence = sentece.replace("i","+")
print(changed_sentence)

print(sentece)

text = 'the better the family, the better the society'
print(text.title())

sentece = "I live and work in Virginia"
swap_case = sentece.swapcase()
print(swap_case)
print(swap_case.capitalize())

text = 'ClaRusWay'
print(text.replace('W','***'))
print(text.replace('W','***').lower())
print(text.replace('W','***').lower().upper())

text ="S0d0me and G0m0re"
print(text.replace('0','o'))

isim = '        Ali           '
print(isim)
print(isim.strip())
meslek = '\n    codder    \t  '
print(meslek.strip())
print(meslek.rstrip())

space_string = "    listen first   "
print(space_string.strip())

text = 'abcdabcd'
print(text.strip('a'))
print(text.strip('ab'))
print(text.strip('ba'))
print(text.strip('bad'))
print(text.strip('badc'))
print(text.strip('c'))

text ='tyou can learn almost everything in pre-classz'
print(text.strip('tz'))
print(text.strip('tz').upper())
print(text.rstrip('z'))
print(text.rstrip('z').lstrip('t'))
print(text.rstrip('z').lstrip('t').upper())

text = 'In God wee Trust'
print(text.replace('wee','we'))

