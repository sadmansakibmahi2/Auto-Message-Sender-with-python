import time
import pyautogui # go to this link to install this library https://pypi.org/project/PyAutoGUI/
msg = 'hello'# your msg
number_of_msg= 35 # number of msg you want to send
count = 0
time.sleep(4)
while number_of_msg>0 :
	number_of_msg = number_of_msg - 1
	count = count + 1
	print(count)
	print(msg)
	pyautogui.write(msg)
	pyautogui.press('enter')
	time.sleep(2)
