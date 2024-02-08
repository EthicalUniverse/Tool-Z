###-------[IMPORT MODULES]-----------####

import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor

###-------[BASIC COLORS]-----------####
reset = "\033[0m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"

###-------[FLASH COLORS]-----------####
colors = ["\033[1;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]

###-------[LOOP]-----------####
loop = 0
idz = []
oks = []
cps = []



###--------[About]----------###
def about():
    clear()
    linex()

    print(f" \033[1;92m*• \033[1;97mAuthor : \033[1;92mKobir Khan")
    print(f" \033[1;92m1• \033[1;97mFacebook : Ethacal Universe")
    print(f" \033[1;92m2• \033[1;97mYoutube : Ethacal Universe")
    print(f" \033[1;92m3• \033[1;97mGithub : Ethacal Universe")
    print(f" \033[1;92m4• \033[1;97mVersion : \033[1;92m1.0")

    print("")
    print("")
    print(f" \033[1;97m[\033[1;92m0\033[1;97m] Back")
    linex()

    abou= input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")
    if abou in ['1','01']:
        os.system("xdg-open https://facebook.com/EthacalUniverse")
        about()

    elif abou in ['2','02']:
        os.system("xdg-open https://youtube.com/")
        time.sleep(3)
        about()

    elif abou in ['3','03']:
        os.system("xdg-open https://www.github.com")
        about()


    elif abou in ['0','00']:
        menu()


    else:
        print(f"\n\033[1;91m Select valid option ...") 
        time.sleep(1)
        about()


###-------[LOGO]-----------####
logo= f'''\033[1;31m
  _  __   ____    ____    _____   _____     __   __
 | |/ /  / __ \  |  _ \  |_   _| |  __ \    \ \ / /
 | ' /  | |  | | | |_) |   | |   | |__) |    \ V / 
 |  <   | |  | | |  _ <    | |   |  _  /      > <  
 | . \  | |__| | | |_) |  _| |_  | | \ \     / . \ 
 |_|\_\  \____/  |____/  |_____| |_|  \_\   /_/ \_\
       '''


###-------[CLEAR TERMINAL]-----------####
def clear():
    os.system("clear")
    print(logo)



###-------[LINE]-----------####
def linex():
    print(f"\033[1;36m====================================================")



###-------[MSIN MENU]-----------####
def menu():
    os.system("clear")
    print(logo)
    linex()


    print(f" \033[1;97m[\033[1;92m01\033[1;97m] All Tool")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] Tool Catagory")
    print(f" \033[1;97m[\033[1;92m03\033[1;97m] About US")


    print(" ")
    print(f" \033[1;97m[\033[1;92mU\033[1;97m] Update Tool-Z")
    print(f" \033[1;97m[\033[1;92mX\033[1;97m] Exit")
    linex()
    
    kobir= input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")
    if kobir in ['1','01']:
        time.sleep(1)
        all_tool();
            
    elif kobir in ['2','02']:
        time.sleep(1)
        Catagory();
        
    elif kobir in ['3','03']:
    	time.sleep(1);about()

    elif kobir in ['u','U']:
        os.system("apt install git")
        menu()

    elif kobir in ['5','05']:
        os.system("apt install lolcat")

    elif kobir in ['6','06']:
        information_gathering()
    

    elif kobir in ['x','X']:
       os.system("exit")

    else:
        print(f"\n\033[1;91m Select valid option ....")
        time.sleep(1)
        menu()
           
    
      

###-------[DEF CLONING]-----------####
def information_gathering():
    clear()
    print(f" \033[1;97m[\033[1;92m01\033[1;97m] Nmap: Utility for network discovery and security auditing")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] Vulnerability Analysis")
    print(f" \033[1;97m[\033[1;92m03\033[1;97m] Web Hacking")
    print(f" \033[1;97m[\033[1;92m04\033[1;97m] Database Assessment")
    print(f" \033[1;97m[\033[1;92m05\033[1;97m] Password Attacks")
    print(f" \033[1;97m[\033[1;92m06\033[1;97m] Wireless Attacks")
    print(f" \033[1;97m[\033[1;92m07\033[1;97m] Reverse Engineering")
    print(f" \033[1;97m[\033[1;92m08\033[1;97m] Exploitation Tools")
    print(f" \033[1;97m[\033[1;92m09\033[1;97m] Reporting Tools")
    print(f" \033[1;97m[\033[1;92m10\033[1;97m] Install Linux Distro")
    print(f" \033[1;97m[\033[1;92m11\033[1;97m] Compiler/Interpreter")
    print(f" \033[1;97m[\033[1;92m12\033[1;97m] Social Engineering Tools")
    print("")
    print("")
    
    print(f" \033[1;97m[\033[1;92m00\033[1;97m] Back to main menu")
    
    
     
    
    tool= input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")


    if tool in ['1','01']:
        menu()
        
        
    elif tool in ['2','02']:
        os.system("xdg-open https://youtube.com/@Ethical_Universe?si=-hQ-Ux5BVpOVtQpB")
        time.sleep(3)
        menu()

    elif tool in ['3','03']:
    	os.system("xdg-open https://www.facebook.com/FBAntorRay");time.sleep(3);information_gathering()       


    if tool in ['4','04']:
    	os.system("apt install git");time.sleep(3);information_gathering()       


    elif tool in ['0','00']:
    	os.system("apt install git")




###--------Tool Catagary--------###
def Catagory():
    clear()
    linex()


    print(f" \033[1;97m[\033[1;92m01\033[1;97m] All")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] Show")
    print(f" \033[1;97m[\033[1;92m03\033[1;97m] Abou")
    print(f" \033[1;97m[\033[1;92m04\033[1;97m] Upda")
    print(f" \033[1;97m[\033[1;92m05\033[1;97m] Tuti")
    print(" ")
    print(" ")
    print(f" \033[1;97m[\033[1;92m0\033[1;97m] Back")

    linex()

    catagory= input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")


    if catagory in ['1','01']:
          os.system("apt update")


    elif catagory in ['0','00']:
          time.sleep(1)
          menu()

    else :
         print("\n\033[1;91m Select valid option ....")
         time.sleep(1)
         Catagory();



###--------Tool Catagary--------###
def all_tool():
    clear()
    linex()


    print(f" \033[1;97m[\033[1;92m01\033[1;97m] All")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] Show")
    print(f" \033[1;97m[\033[1;92m03\033[1;97m] Abou")
    print(f" \033[1;97m[\033[1;92m04\033[1;97m] Upda")
    print(f" \033[1;97m[\033[1;92m05\033[1;97m] Tuti")
    print(" ")
    print(" ")
    print(f" \033[1;97m[\033[1;92m0\033[1;97m] Back")

    linex()

    all= input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")


    if all in ['1','01']:
          os.system("apt update")


    elif all in ['0','00']:
          time.sleep(1)
          menu()

    else :
         print("\n\033[1;91m Select valid option ....")
         time.sleep(1)
         all_tool();
         
         
         
###---------home--------##
menu()
