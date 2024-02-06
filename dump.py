#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf mdump.so mdump32.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('mdump.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/mdump.cpython-311.so?raw=true -o mdump.so')
        from mdump import main_menu
        main_menu()
    else:
        from mdump import main_menu
        main_menu()
elif bit == '32bit':
    if not os.path.isfile('mdump32.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/mdump32.cpython-311.so?raw=true -o mdump32.so')
        from mdump32 import main_menu
        main_menu()
    else:
        from mdump32 import main_menu
        main_menu()
else:
    print ('Your device is not supported ')
    exit()
