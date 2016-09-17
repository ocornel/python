'''This converts a given decimal value to a chosen base'''
def Convert(decimal, base):
	xbase = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if type(decimal) == int and type(base) == int and base in range(2, 37):
		reslist = []
		deci = decimal
		while deci > 0:
			reslist.append(xbase[deci % base])
			deci //= base

		result = ''.join(reslist)[::-1]
		print(decimal, 'to base', base, 'is', result)

	else:
		print("Ensure both the decimal and the base are integers and base in range 2 to 36.")