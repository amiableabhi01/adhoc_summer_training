#!/usr/bin/python3
import time 
import webbrowser
import subprocess
menu='''
press 1 to check current time and date :
press 2 to scan all ur mac adresses in ur current connected network :
press 3 to shutdown ur machine after 15 min :
press 4 to search something on google :
press 5 to lgout ur current machine :
press 6 to shutdown all connected sysytem in ur current network :
press 7 to update ststus in fb :
press 8 to list ip address of given website :
'''
print(menu)
choice=input()

if choice == '1' :
    print("current date and time is :",time.ctime())
elif choice == '4':
	find=input("enter ur query: ")
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)
if choice == '2':
   mac_add=subprocess.getoutput("cat /sys/class/net/*/address")
   print(mac_add)
else :
    print("invalid option")
