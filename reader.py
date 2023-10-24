ith open("sample.ini") as file:
        x = file.read()

def variables(x):
     for line in x.split('\n'):
        print(line)
        
        lineHalf = line.split("=")
        print(lineHalf[0])
       
    
variables(x)
