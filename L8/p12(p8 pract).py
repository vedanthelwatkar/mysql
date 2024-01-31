'''wapp to find
1) names of students
2)names of common students
3)students in java but not in js
4)students in js but not in java
'''
java={"prachi","nidhi","khushi","preeti","sneha"}
js={"vidhi","prachi","khushi"}

r1=java|js
print(r1)
r2=java&js
print(r2)
r3=java-js
print(r3)
r4=js-java
print(r4)