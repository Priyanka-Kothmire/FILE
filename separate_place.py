people=open("people_exercice.txt","r")
for i in range (30):
    # print(c)
    c=people.readline()
    # print(c)
    if "delhi" in c:
        delhi=open("delhi.txt","a")
        delhi.write(c)
    elif "shimla" in c:
        shimla=open("shimla.txt","a")
        shimla.write(c)
    else:
        others=open("others.txt","a")
        others.write(c)
people.close()



    



















