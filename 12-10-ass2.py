sno=int(input("enter sno:"))
sname=(input("enter sname:"))
group=(input("enter group:"))
s1=int(input("enter s1:"))
s2=int(input("enter s2:"))
s3=int(input("enter s3:"))
avg=(s1+s2+s3)/3
if avg>=90:
    print('O-grade')
elif avg>=80:
    print('A-grade')
elif avg>=70:
    print('B-grade')
elif avg>=60:
    print('C-grade')
elif avg>=50:
    print('D-grade')
else:
 print('pass')
