a=int(input("Enetr 1st Number:"));
b=int(input("Enetr 2nd Number:"));
c=int(input("Enetr 3rd Number:"));
d=int(input("Enetr 4rd Number:"));
e=int(input("Enetr 5th Number:"));
total=a+b+c+d+e;
percent=(total/500)*100;
print("total marks=",total,);
print("percetage=",percent);
if percent>=80:
        print("you have got Grade.A");
elif percent>=60:
        print("you have got Grade.B");
elif percent>=40:
        print("you have got Grade.C");
else:
    print("you have got Grade.D");
