def gcd(a,b):
	lim = min(a,b)
	gcd = 0
	while lim > 0:
		if a % lim == 0 and b % lim == 0:
			gcd = lim
			break
		else:
			lim -= 1
	return(gcd)

def fraction(decimal):

	pow = len(str(decimal))
	if pow > 6:
		print(decimal, "is quite a long number. Will take a while to calculate. Please wait.\n Press Ctrl + c if you wish to cancel.")
	denom = 10 ** pow
	numer = decimal * denom
	w = numer // denom
	n = int((numer % denom)/gcd(numer, denom))
	d = int(denom/gcd(numer, denom))
	if w == 0:
		result = "%s as a fraction is %d/%d" %(str(decimal), n, d)
	elif n == 0:
		result = "%s is a whole number %d" %(str(decimal), w)

	else:
		result = "%s as a fraction is %d and %d/%d \n" %(str(decimal), w, n, d)
	return(result)