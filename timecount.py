#! /usr/bin/env python3

import time

instructions = ' '
time_passed = 0


while True:
	instructions = input('Enter "start" to start counting:')
	if instructions == 'start':
		startTime = time.time()

	instructions = input('Enter "pasue" to pause counting, "end" to stop counting:')
	if instructions == 'pause':
		pauseTime = time.time()
		time_passed += round(pauseTime - startTime, 2)
		print(str(time_passed) + ' seconds has passed')
		continue
	elif instructions == 'end':
		endTime = time.time()
		time_passed += round(endTime - startTime, 2)
		break

print(str(time_passed) + ' seconds has passed')


	

	