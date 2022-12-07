#Sean Maida

def assembler(file):
    """Input: assembly program as a .txt file
          Output: image file"""
    program = open(file, "r")
    length = program.readlines() #number of lines in program
    lst = [[] for _ in range(len(length) - 1)]
    b = 0 #binary encoding
    
    #Converts to Machine Code
    for i in range(len(length) - 1):
        instruction = length[i].split()
        if (instruction[0] == "LOAD"):
            b_ = "01000000"
            if(instruction[1] == "X1,"):
                b_ = "01000001"
            if(instruction[1] == "X2,"):
                b_ = "01000010"
            if(instruction[1] == "X3,"):
                b_ = "01000011"
            lst[i].append(b_)
            lst[i].append(instruction[1])
            lst[i].append(int(instruction[2]))
        if(instruction[0] == "PLUS"):
            b = 10000000
            if(instruction[1] == "X0,"):
                b = b + 0
            if(instruction[1] == "X1,"):
                b = b + 1
            if(instruction[1] == "X2,"):
                b = b + 10
            if(instruction[1] == "X3,"):
                b = b + 11
            if(instruction[2] == "X1,"):
                b = b + 100
            if(instruction[2] == "X2,"):
                b = b + 1000
            if(instruction[2] == "X3,"):
                b = b + 1100
            if(instruction[3] == "X1"):
                b = b + 10000
            if(instruction[3] == "X2"):
                b = b + 100000
            if(instruction[3] == "X3"):
                b = b + 110000
            lst[i].append(b)
            lst[i].append(instruction[2])
            lst[i].append(instruction[3])
        if(instruction[0] == "MINUS"):
            b = 11000000
            if(instruction[1] == "X0,"):
                b = b + 0
            if(instruction[1] == "X1,"):
                b = b + 1
            if(instruction[1] == "X2,"):
                b = b + 10
            if(instruction[1] == "X3,"):
                b = b + 11
            if(instruction[2] == "X1,"):
                b = b + 100
            if(instruction[2] == "X2,"):
                b = b + 1000
            if(instruction[2] == "X3,"):
                b = b + 1100
            if(instruction[3] == "X1"):
                b = b + 10000
            if(instruction[3] == "X2"):
                b = b + 100000
            if(instruction[3] == "X3"):
                b = b + 110000
            lst[i].append(b)
            lst[i].append(instruction[2])
            lst[i].append(instruction[3])
    
    #Converts machine code to hexadecimal and creates the image file
    lst2 =  [[] for _ in range(len(length) - 1)] #empty list to store values of lst as hexadecimal
    image = open("image file", "w", encoding='utf-8')
    count = 0
    for i in range(len(length) - 1):
        y = lst[i][0]
        instruction = length[i].split()
        if(isinstance(y, str) == True):
            if(y[:2] == "01"):
                z = lst[i][1]
                z = z.replace(",", "")
                z = z[-1]
                lst2[i].append(hex(int(z)).replace("x", ""))
                image.write(hex(int(z)).replace("x", "") + " ")
                count = count + 1
                lst2[i].append(hex(int(instruction[2]))[1:4].replace("x",""))
                image.write(hex(int(instruction[2]))[1:4].replace("x","") + " ")
                count = count + 1
            if(count == 16):
                image.write("\n")
                count = 0
            if(i != len(length) - 2):
                if(len(lst2[i]) == 3):
                    for j in range(3):
                        image.write("00" + " ")
                        count = count + 1
                        if(count == 16):
                            image.write("\n")
                            count = 0
                if(len(lst2[i]) == 2):
                    for j in range(4):
                        image.write("00" + " ")
                        count = count + 1
                        if(count == 16):
                            image.write("\n")
                            count = 0
        if(str(lst[i])[1:3] == "10" or str(lst[i])[1:3] == "11"):
            s = int(str(lst[i])[1:3])
            lst2[i].append(s)
            image.write(str(s) + " ")
            z = lst[i][1]
            z = z.replace(",", "")
            z = z[-1]
            lst2[i].append(hex(int(z)).replace("x",""))
            image.write(hex(int(z)).replace("x","") + " ")
            count = count + 1
            z = lst[i][2]
            z = z.replace(",", "")
            z = z[-1]
            lst2[i].append(hex(int(z)).replace("x",""))
            image.write(hex(int(z)).replace("x","") + " ")
            count = count + 1
            if(count == 16):
                image.write("\n")
                count = 0
            if(i != len(length) - 2):
                if(len(lst2[i]) == 3):
                    for j in range(3):
                        if(count == 16):
                            image.write("\n")
                            count = 0
                        image.write("00" + " ")
                        count = count + 1
                if(len(lst2[i]) == 2):
                    for j in range(4):
                        image.write("00" + " ")
                        count = count + 1
                        if(count == 16):
                            image.write("\n")
                            count = 0
    if(count < 16):
        for i in range(15 - count):
            image.write("00" + " ")
    image.close()
    program.close()    
