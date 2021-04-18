N =  int(input())
for _ in range(N):
    T = int(input())
    if T >= 2015:
	print("%d A.C."%(T-2015+1))
    else:
	print("%d D.C."%(2015-T))
