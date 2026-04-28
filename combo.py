T=int(input("enter ure  T score"))
E=int(input("enter ure E  score"))
M=int(input("enter ure M  score"))
S=int(input("enter ure S  score"))
SS=int(input("enter ure  SS score"))
Avg=T+E+M+S+SS
Avg/=5
if(Avg>=95 and Avg<=100):
    print("HURRAY! U HAVE PASSED WITH DISTINCTION",Avg,"%")
elif(Avg>=75 and Avg<95):
    print("CONGRATS! U HAVE PASSED WITH good results",Avg,"%")  
elif(Avg>=35 and Avg<75):
    print("HURRAY! U HAVE PASSED WITH AVG SCORE",Avg,"%")
else:
    print("sorry u have not passed",Avg,"%")

      
