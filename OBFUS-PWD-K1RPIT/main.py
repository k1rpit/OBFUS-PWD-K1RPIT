from sys import argv,exit
from rich import print
from toolOBFUS.obfus import *


sys_argv = argv[1:]



def main(*,arg: list):
    try:
        if arg[0] == '-lo' or arg[0] == '--lite-obfus':
            result = lite_obfus(pwd=sys_argv[1])
        elif arg[0] == '-no' or arg[0] == '--normal-obfus':
            result = normal_obfus(pwd=sys_argv[1])
        elif arg[0] == '-ho' or arg[0] =='--hard-obfus':
            result = hard_obfus(pwd=sys_argv[1])
        elif arg[0] == '--help' or arg[0] ==  '-h':
            print('''[red]
            -lo or --lite-obfus\tInvert case, append random 4-digit number and punctuation sign;
            -no or --normal-obfus\tTransform word core via mirror-map with double random tail;
            -ho or --hard-obfus\tExtreme mutation via dynamic initialization map and random UUID slice;

            syntax:python3 main.py <argv> <word>
            ''')
        else:
            print('''[red]
            syntax:python3 main.py <argv> <word>
            for help, enter "--help"
            ''')
    except IndexError:

            print('''[red]
            syntax:python3 main.py <argv> <word>
            for help, enter "--help"
            ''')
            exit('no argv!')
    return result

   
        
if __name__ == "__main__":
    try:
        print('--'*32)
        print(f'[blue]\t{main(arg=sys_argv)}')
        print('--'*32)
    except UnboundLocalError:
        exit()

