'''wapp to find
1) names of students
2)names of common students
3)students in java but not in js
4)students in js but not in java
'''
#java=set()
java={"amit","neha","pooja"}
js={"amit","rahul"}

#r1=java|js;   #print(r1)
#r1=java.union(js)
r1=java|js
print(r1)

#java.intersection(js)
r3=java&js
print(r3)

r4=java-js
print(r4)

r5=js-java
print(r5)