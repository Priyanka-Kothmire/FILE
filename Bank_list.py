bank_list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
a=open("bank_list1","w")
i=0
while i<len(bank_list):
    a.write(bank_list[i])
    a.write("\n")
    i=i+1
a.close()





