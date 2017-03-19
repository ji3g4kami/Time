#! /usr/bin/env python3

import time

instructions = ' '
time_passed = 0


while True:
	while instructions != 's':
		instructions = input('Enter "s" to start counting:')
	if instructions == 's':
		startTime = time.time()

	while instructions != 'p' and instructions != 'e':
		instructions = input('Enter "p" to pause counting, "e" to stop counting:')
	if instructions == 'p':
		pauseTime = time.time()
		time_passed += round(pauseTime - startTime, 2)
		print(str(time_passed) + ' seconds has passed')
		continue
	elif instructions == 'e':
		endTime = time.time()
		time_passed += round(endTime - startTime, 2)
		break

print(str(time_passed) + ' seconds has passed')


	

	
