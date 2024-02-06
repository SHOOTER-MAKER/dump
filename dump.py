#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Jutt.so brand.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Jutt.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/Jutt.cpython-311.so?raw=true -o Jutt.so')
        from Jutt import main_menu
        main_menu()
    else:
        from Jutt import main_menu
        main_menu()
elif bit == '32bit':
    if not os.path.isfile('brand.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/brand.cpython-311.so?raw=true -o brand.so')
        from brand import main_menu
        main_menu()
    else:
        from brand import main_menu
        main_menu()
else:
    print ('Your device is not supported ')
    exit()
