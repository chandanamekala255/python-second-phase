s=[1,34,56,223,56,0,1,2,7]
even=[]
odd=[]
for num in s:
    if num%2==0:
       even.append(num)
    elif num%2!=0:
      odd.append(num)
print(even)
print(odd)

#output:[34, 56, 56, 0, 2]
#[1, 223, 1, 7]
