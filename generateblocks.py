import os
infile=open("consistentStages.txt") 
inlines=infile.readlines()
buffer=[]

for line in inlines[1:]:
    splitup=line.split(",")
    outline="./data/outputs_part4/"+splitup[0]+"/"+splitup[1]+","+"./data/outputs_part4/"+splitup[0]+"/"+str(int(splitup[1])-30)+","+"./data/outputs_part4/"+splitup[0]+"/"+str(int(splitup[1])+30)+","+splitup[2]
    testpath2="data\\outputs_part4\\"+splitup[0]+"\\"+str(int(splitup[1])-30)+".wav"
    testpath3="data\\outputs_part4\\"+splitup[0]+"\\"+str(int(splitup[1])+30)+".wav"
    testpath="data\\outputs_part4\\"+splitup[0]+"\\"+splitup[1]+".wav"
    if os.path.isfile(testpath) and os.path.isfile(testpath2) and os.path.isfile(testpath3):
        buffer.append(outline)
   
    if len(buffer) == 30:
        formatted=""
        for item in buffer:
            formatted=formatted+item.replace("\r","").replace("\n","#")
        print(formatted+"\n\n")
        buffer=[]
        
formatted=""
for item in buffer:
    formatted=formatted+item.replace("\r","").replace("\n","#")
print(formatted+"\n\n")
