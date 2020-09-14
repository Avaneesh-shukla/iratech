#1

#Method 1 : Iteration
def summation(x,n):
    s=0
    for i in range(1,n+1):
        s+=(1/(x**i))
    return s
n,x=map(int,input().split())
print(summation(x,n))

#Method 2 : Recursion
def rec(x,n,s):
    if n==0:
        return s
    s+=(1/(x**n))
    return rec(x,n-1,s)
print(rec(x,n,0))

#2
def next_num(li):
	fir = li[-2]
	sec = li[-3]
	thir = li[-1]
	to_add = fir-sec+4
	return thir+to_add
	
data = list(map(int, input().split()))
print(next_num(data))

#3
x,y,a,b=map(int,input().split())
def expression (x,y,a,b):
    try:
        ans=(((x+(1/y))**a)*((x-(1/y))**b))/(((y+(1/x))**a)*((y-(1/x))**b))
    except:
        return "divide by zero"
    return ans
print(expression (x,y,a,b))
