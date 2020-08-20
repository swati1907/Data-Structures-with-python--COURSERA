
     

pattern=input()
text=input()
p=ord(pattern[0])
result=[]
for i in range(0,len(text)-len(pattern)+1):
    #print(i,ord(text[i]),p)
    if ord(text[i])==p:
        
        if text[i:len(pattern)+i]== pattern:
            result.append(i)
for i in result:
    print(i,end=" ")
