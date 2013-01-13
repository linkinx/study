'''
Created on Jan 10, 2013

@author: linkinx
'''
import easygui
import string
numbers = 0
letters = 0
guid = easygui.enterbox("Guid?: ")
for letter in guid:
    if letter in string.ascii_letters:
        letters += 1
    elif string.digits:
        numbers += 1
total = letters + numbers
guidfile = open("GUID.txt", 'a+b')
guidfile.write('{0} >>>>>> {1}digits\n'.format(guid, total))
guidfile.close()
