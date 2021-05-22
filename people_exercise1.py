people=open("people_exercice.txt","r")
count=0
for i in (people):
    count=count+1
print(count)
people.close()