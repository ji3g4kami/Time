#! /usr/bin/env python3

import time

instructions = 'end'

instructions = input('Enter "start" to start counting:')
if instructions == 'start':
	startTime = time.time()

instructions = input('Enter "end" to stop counting:')
if instructions == 'end':
	endTime = time.time()

time_passed = round(endTime - startTime, 2)

print(str(time_passed) + ' seconds has passed')


	

	