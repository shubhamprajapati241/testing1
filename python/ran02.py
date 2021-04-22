# Random no generation by congruvent method
x=int(input("type the value of seed"))
for i in range(1,100,2):
    y=(x*i+654)%0.255
    z=round(y,4)
    z_str=str(z)
    f=open("ran02.txt","a")
    f.write(z_str+"\n")
5f.close()    