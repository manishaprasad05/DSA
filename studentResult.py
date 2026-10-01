#student roll,DSA,AI,DBMS,React,SAD
#create function result pass value using object .
#result function retuns pass or fail 
#if pass return % if fail return - ,if  marks >=40 to pass otherwise fail.
class Student:

    def result(self, roll, DSA, AI, DBMS, React, SAD):

        if dsa >= 40 and AI >= 40 and DBMS >= 40 and React >= 40 and SAD >= 40:
            total = DSA + AI + DBMS + React + SAD
            per = total / 5
            return "Pass", per
        else:
            return "Fail", "-"


s1= Student()
result = s1.result(101, 60, 70, 50, 80, 65)

print("Roll No:", 101)
print("Result:", result[0])

if result[0] == "Pass":
    print("Percentage:", result[1], "%")
else:
    print("Percentage:", result[1])
