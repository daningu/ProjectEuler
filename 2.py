def fibseq(n):
	if n == 1 or n == 2:
		return 1
	return(fibseq(n-1)+fibseq(n-2))
#print fibseq(7)
i = 1
evensum = 0
while fibseq(i) < (4*10**6):
	if fibseq(i)%2 == 0:
		evensum += fibseq(i)
	i += 1
print (evensum)