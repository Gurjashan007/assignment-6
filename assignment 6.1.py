#Q1
def is_perfect_number(n):
    sum=0
    sum_all=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            sum_all+=i
    sum2=(sum_all+n)//2        
    return sum==n , sum2==n
p=int(input())
print(is_perfect_number(p))

