import secrets
import uuid
import string


replacement_dictionary_normal = {
    'a':'@','b':'d','d':'b','c':'[',
    'i':'1','s':'$','0':'o','o':'0',
    '1':'i','.':',','3':'#','h':'|',
    'q':'o|','w':'\|/','e':'E','r':'[o'
}

replacement_dictionary_hard = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
     'a': secrets.choice(list(string.punctuation)) + secrets.choice(list(string.hexdigits)),
    's': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'd': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'f': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'g': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'h': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'j': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'k': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'l': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '!': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '@': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '#': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '$': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '%': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '^': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '&': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '*': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '(': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    ')': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '_': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    '+': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
    'q': secrets.choice(list(string.punctuation))+ secrets.choice(list(string.hexdigits)),
}

def lite_obfus(*,pwd: str) -> tuple:
    new_pwd = pwd.swapcase()
    return '{}{}{}'.format(new_pwd,secrets.choice(list(range(9999))),secrets.choice(list(string.punctuation))),pwd



def normal_obfus(*,pwd: str,replacement_dictionary=replacement_dictionary_normal) -> tuple:
    new_pwd = pwd.lower()
    for key,value in replacement_dictionary.items():
        new_pwd=new_pwd.replace(f'{key}',f'{value}')
    return '{}{}{}{}'.format(new_pwd,secrets.choice(list(range(9999))),secrets.choice(list(string.punctuation)),secrets.choice(list(string.punctuation))),pwd




def hard_obfus(*,pwd: str,replacement_dictionary=replacement_dictionary_hard) -> tuple:
    new_pwd = pwd.lower()
    for key,value in replacement_dictionary.items():
        new_pwd=new_pwd.replace(f'{key}',f'{value}')
    new_pwd = new_pwd.capitalize() + str(uuid.uuid4())[::secrets.choice(list(range(1,10)))] + secrets.choice(list(string.punctuation))
    return new_pwd,pwd
