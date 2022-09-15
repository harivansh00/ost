#fibonacci series 
interms=int(input("How many terms? ="))
# first two terms
n1, n2 = 0 , 1
count = 0 
if nterms <=0:
     print("Please enter a postive interger")
elif nterms==1:
     print("fibonacci sequence upto ",nterms,":")
else:
     print("fibonacci sequence:")
     while count<nterms:
             print(n1)
             nth=n1+n2
             n1=n2
             count+=1
             