def allot(count):
	counts = count

	time = 5

	if counts>0:
		if count<10:
			time += 10

		elif count<20:
			time += 20

		elif count<30:
			time += 40

		elif count<40:
			time += 60

		elif count<50:
			time += 80

		elif count<60:
			time += 100

		elif count<70:
			time += 110

		else:
			time = 120


	return time

	