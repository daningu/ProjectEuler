N = 10^11
mod = 998244353
total = [0]
for i in xrange(1,N+1):
    for j in xrange(1,i+1):
        total[0] = pow(total[0] + gcd(i,j),1,mod)


print total
