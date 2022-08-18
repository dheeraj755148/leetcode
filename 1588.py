nums = [5,4,6,3]
profits = [10,40,30,50]
limit = 10
s = 0
m = 0
ans = {}
ans_points = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if((nums[i]+nums[j])<=limit):
            s = profits[i]+profits[j]
            print(s,i,j)
            if(s>m):
                m=s
print("Max profit=> ",m)