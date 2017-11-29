from gpiozero import RGBLED, Button
from time import sleep

led1 = RGBLED(14,15,18)
led2 = RGBLED(23,24,25)
led3 = RGBLED(8,7,12)

button = Button(21)

mode1 = (1, 0, 0) # Red
mode2 = (0, 1, 0) # Green

while True:	
	led1.on()
	led2.on()
	led3.on()

	button.wait_for_press()
	button.wait_for_release()

	led1.blink()
	sleep(0.4)
	led2.blink()
	sleep(0.4)
	led3.blink()

	button.wait_for_press()
	button.wait_for_release()
	
	led1.pulse()
	sleep(0.4)
	led2.pulse()
	sleep(0.4)
	led3.pulse()
	
	button.wait_for_press()
	button.wait_for_release()
	
	led1.on()
	led2.color(mode1)
	led3.color(mode2)
	
	button.wait_for_press()
	button.wait_for_release()
	
	led1.blink(on_color=(mode1), off_color=(mode2))
	sleep(0.4)
	led2.blink(on_color=(mode2), off_color=(mode1))
	sleep(0.4)
	led3.blink(on_color=(mode1), off_color=(mode2))
	
	button.wait_for_press()
	button.wait_for_release()
	
	led1.pulse(on_color=(mode1), off_color=(mode2))
	sleep(0.4)
	led2.pulse(on_color=(mode2), off_color=(mode1))
	sleep(0.4)
	led3.pulse(on_color=(mode1), off_color=(mode2))