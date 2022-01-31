import time
import random
import pyautogui # go to this link to install this library https://pypi.org/project/PyAutoGUI/
msg_list =["How are you?","how old are you?","What is your age?","Where are you from"]          # your msg
number_of_msg= 35 # number of msg you want to send
count = 0
time.sleep(4)
while number_of_msg>0 :
	number_of_msg = number_of_msg - 1
	count = count + 1
	msg= random.choice(msg_list)
	print(count)
	print(msg)
	pyautogui.write(msg)
	pyautogui.press('enter')
	time.sleep(1)
