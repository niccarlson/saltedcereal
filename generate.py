# 13 digits
# first digit represents family
# second digit is reserved for now
# next 11 digits are actual serial number (-s) numbered 0-10
# even digits of -s have to add up to 11 + pi(family)(rounded)=flavor(even) - 0 is considered even
# odd digits of -s have to add up to 16+family=flavor(odd)
# now shift -s by family number
# add family number by +4 (9->3)
# now change reserve to [7] of -s, and [7] of -s to current family number minus ones digit of all odd digits -s multiplied excluding zeroes and family number+2, and then multiply by -s[8]
# shift whole thing by 4


#  i: 0		1		2		3		4		5		6		7		8		9		10		11		12

#  i: -		-		0		1		2		3		4		5		6		7		8		9		10
# ex: 7		_		x		x		x		x		x		x		x		x		x		x		x
# flavor(even) = 11+pi(7) = 33
# flavor(odd) = 16+family = 23
# ex: 7		_		9		4		3		7		7		0		6		4		5		8		3
# ex: 7		_		7		0		6		4		5		8		3		9		4		3		7
# ex: 1		_		7		0		6		4		5		8		3		9		4		3		7
# ex: 1		9		7		0		6		4		5		8		3		x		4		3		7
# ex: 1		9		7		0		6		4		5		8		3		8		4		3		7






import random
import math
from collections import deque
def generateSerial():
	serial = deque([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	family = random.randint(0,9)
	serial[0] = family
	while True:
		digitO = random.randrange(3, 11, 2)
		serial[digitO] = random.randint(0,9)
		if (serial[3] + serial[5] + serial[7] + serial[9] + serial[11] == (16 + family)):
			break
	while True:
		digitE = random.randrange(2, 12, 2)
		serial[digitE] = random.randint(0,9)
		if (serial[2] + serial[4] + serial[6] + serial[8] + serial[10] + serial[12] == math.floor(11 + math.pi*family)):
			break
	serial.rotate(family)
	serial[0] = (family + 4) % 10
	serial[1] = serial[9]
	pepper = 1
	for i in range(5):
		index = ((i + 1) * 2) + 1
		current = serial[index]
		if index == 9:
			current = serial[10]
		if serial[index] != 0 and serial[index] != (family + 2):
			pepper *= current
	serial[9] = serial[0] - (pepper % 10)
	serial.rotate(4)
	return serial

def decodeSerial(serialN):
	serialN.rotate(-4)
	serialN[9] = serial[1]
	serialN[0] = 10 - serialN[0]

print(generateSerial())