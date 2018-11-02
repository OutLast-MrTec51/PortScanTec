#coding: utf-8
#ScriptingByOficial: MalwareTec
#ByKoded: ↓
#OutLast
#NOCIVO

import socket
from os import *
from time import *
	
sleep( 2 )
system("clear")


print("\033[1;31m██\033[1;33m╗  \033[1;31m██\033[1;33m╗ \033[1;31m██████\033[1;33m╗ \033[1;31m███████\033[1;33m╗\033[1;31m██████\033[1;33m╗ \033[1;31m██\033[1;33m╗")
print("\033[1;31m██\033[1;33m║  \033[1;31m██\033[1;33m║\033[1;31m██\033[1;33m╔═══\033[1;31m██\033[1;33m╗\033[1;31m██\033[1;33m╔════╝\033[1;31m██\033[1;33m╔══\033[1;31m██\033[1;33m╗\033[1;31m██\033[1;33m║")
print("\033[1;31m███████\033[1;33m║\033[1;31m██\033[1;33m║   \033[1;31m██\033[1;33m║\033[1;31m███████\033[1;33m╗\033[1;31m██████\033[1;33m╔╝\033[1;31m██\033[1;33m║")
print("\033[1;31m██\033[1;33m╔══\033[1;31m██\033[1;33m║\033[1;31m██\033[1;33m║   \033[1;31m██\033[1;33m║╚════\033[1;31m██\033[1;33m║\033[1;31m██\033[1;33m╔═══╝ \033[1;31m██\033[1;33m║")
print("\033[1;31m██\033[1;33m║  \033[1;31m██\033[1;33m║╚\033[1;31m██████\033[1;33m╔╝\033[1;31m███████\033[1;33m║\033[1;31m██\033[1;33m║     \033[1;31m██\033[1;33m║")
print("\033[1;33m╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝")
print("\033[1;36mScriptingKoded: \033[1;33m[\033[1;35m\033[1;31mOutLast\033[1;33m/\033[1;34mNocivo\033[1;33m/\033[1;32mFox\033[1;33m]\n")
print("\033[1;7;35mByTeam:\033[0m \033[1;32mArea 51")
print("\033[1;7;35mByTeam:\033[0m \033[1;32mMalwareTec")
print("\n\033[1;7;33mDIGITE O HOST OU IP PRO SCANNER DE IP/PORTAS !\033[0m\n")
Host = input("\033[1;7;36m@IP/HOST:\033[0m\033[0;33m ")
ipgetost = socket.gethostbyname(Host)
print("\n\033[1;7;32mVERIFICANDO E SCANNEANDO O IP AGORA, AGUARDE !\033[0m\n")
sleep( 2 )
print("\033[1;7;37mIP ADRESS:\033[0m \033[1;33m{}".format(ipgetost))
print("\033[1;7;37mSITE ADRESS:\033[0m \033[1;33m{}".format(Host))
print("\033[1;7;37mScanneando Portas Abertas !\n")
sleep( 1 )

for portys in range(0,16500):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout (0.1)
	if s.connect_ex((ipgetost,portys)):
		s.close()
	else:
	   print("\033[1;7;37mPORTA ABERTA\033[0m\033[1;31m ==\033[1;36m>> \033[1;7;33m{}\033[0m".format(portys))
    
    