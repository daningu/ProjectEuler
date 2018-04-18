# check if forward == backward
def checkpalindrome(n):
	flag = True
	digits = []
	digits = [int(x) for x in str(n)]
	for i in range(len(digits)):
		if digits[i] != digits[len(digits)-1-i]:
			return False
	return True


# generate products
pal = [0]
for i in range(999,0,-1):
	for j in range(999,0,-1):
		prod = i*j
		if checkpalindrome(prod) == True:
			if prod > pal[0]:
				pal[0] = prod
print pal

