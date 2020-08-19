import pyttsx3
import os

while true:
print("WELCOME!! Name your program:" , end=' '))
i= input()


if (("run" in i) or ("start" in i) or ("launch" in i) or ("open" in i)) or (("chrome" in i) or ("browser" in i) or ("web" in i)):
    os.system("chrome")
 elif (("run" in i) or ("start" in i) or ("launch" in i) or ("open" in i)) or (("notepad" in i) or ("editor" in i)):
    os.system("notepad")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("explorer" in i) or ("internet explorer" in i)):
    os.system("iexplore")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("firefox" in i) or ("mozilla" in i)):
   os.system("Mozilla Firefox")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("powerpoint" in i) or ("ppt" in i)):
    os.system("POWERPNT")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("msexcel" in i) or ("excel" in i)):
    os.system("EXCEL")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or ("word" in i):
    os.system("WINWRD")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("cal" in i) or ("calculator" in i)):
   os.system("calc") 
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("vlc" in i) or ("player" in i) or ("mediaplayer" in i)):
    os.system("vlc")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or (("paint" in i) or ("draw" in i)):
    os.system("mspaint")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or ("virtual box" in i):
    os.system("Oracle VM VirtualBox")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or ("zoom" in i):
    os.system("zoom")
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or ("linkedin" in i):
    os.system("chrome linked.in")  
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or ("yt" in i) or ("youtube")):
    os.system("chrome youtube.com")  
 elif (("run" in i) or ("start" in i) or ("launch" in i)) or ("open" in i)) or ("mail" in i) or ("gmail")):
    os.system("chrome gmail.com") 
 elif (("quit" in i) or ("close" in i) or ("exit" in i)):
  break
  
  else:
   print("PLEASE TRY AGAIN")
  
 
