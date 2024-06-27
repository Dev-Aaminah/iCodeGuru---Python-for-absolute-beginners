num = 1
while(num<=5):
    print(num)
    num+=1
    
# Table of 2
i=1
multiple=2
while(i<=10):
    print(multiple , 'x' , i, '=', multiple*i)
    i+=1
    

# Break
new_num =1
while(new_num<=5):
    print(new_num)
    if(new_num==3):
        break
    new_num+=1
    
# continue
print("Even Numbers");
n=1;
while(n<=5):
    if(n%2==0):
        print(n , 'Even');
    n+=1;