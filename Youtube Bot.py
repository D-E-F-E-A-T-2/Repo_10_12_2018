import webbrowser
import os
import time
while True:
	webbrowser.open("https://www.youtube.com/watch?v=Cg8sbRFS3zU") #replace the address with your own video
	time.sleep(120)
	os.system("TASKKILL /F /IM firefox.exe")
