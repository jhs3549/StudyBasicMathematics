s0 = 1
t0 = 0
s1 = 0
t1 = 1

def Extended_Euclidean_Algorithm(a,b):
	global s0, t0, s1, t1
	
	if a % b == 0:
		gcd = b

	else:
		tmps = s0
		tmpt = t0
		s0 = s1
		t0 = t1
		s1 = tmps - int(a/b)*s1
		t1 = tmpt - int(a/b)*t1
		gcd = Extended_Euclidean_Algorithm(b, a%b)

	return gcd

a, b = int(input("a: ")), int(input("b: "))
print(f"gcd = {Extended_Euclidean_Algorithm(a,b)}")
print(f"    = {s1}*{a} + {t1}*{b}")