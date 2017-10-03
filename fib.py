import timeit

def fibonacci(n):
	fibList = []
	for i in range (0, n):
		if i < 2:
			fibList.append(1)
			continue
		fibList.append(fibList[i-1] + fibList[i-2])
	return fibList[n-1]

fibSolved = {}
def fibrec(n, fibSolved):
	if n < 2:
		fibSolved[n] = 1
		return 1
	if n-1 not in fibSolved:
		fibSolved[n-1] = fibrec(n-2, fibSolved) + fibrec(n-3, fibSolved)
	ret1 = fibSolved[n-1]
	if n-2 not in fibSolved:
		fibSolved[n-2] = fibrec(n-3, fibSolved) + fibrec(n-4, fibSolved)
	ret2 = fibSolved[n-2]
	return ret1 + ret2
#timeNow = time()

def fibrec2(n, fibSolved):
	#print fibSolved
	if n < 2:
		fibSolved[n] = 1
		return 1
	if n-1 not in fibSolved:
		if n-2 in fibSolved:
			fib2back = fibSolved[n-2]
		else:
			fib2back = fibrec2(n-2, fibSolved)
		if n-3 in fibSolved:
			fib3back = fibSolved[n-3]
		else:
			fib3back = fibrec2(n-3, fibSolved)
		fibSolved[n-1] = fib2back + fib3back
	ret1 = fibSolved[n-1]
	if n-2 not in fibSolved:
		if n-4 in fibSolved:
			fib4back = fibSolved[n-4]
		else:
			fib4back = fibrec2(n-4, fibSolved)
		fibSolved[n-2] = fib3back + fib4back
	ret2 = fibSolved[n-2]
	return ret1 + ret2

start = timeit.default_timer()

print fibrec(1995, {})
#print fibrec2(1995, {})

#print fibonacci(600000)

#print fibSolved

stop = timeit.default_timer()

print "time: ", stop - start
