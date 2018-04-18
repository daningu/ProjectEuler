def if_prime(n):
    if n==2 or n==3: 
    	return True
    if n%2==0 or n<2: 
    	return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    

    return True

#factoring from largest
x = 600851475143
# print(if_prime(29))
for g in xrange(int(x**.5)+1,2,-1):
	if if_prime(x/g) == True:

		
