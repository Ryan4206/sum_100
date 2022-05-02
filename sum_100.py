
# Online Python - IDE, Editor, Compiler, Interpreter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
between = [0, 0, 0, 0, 0, 0, 0, 0,]
operators = ["+", "-", ""]
target = 100

for i in range(3**8-1):
    between[0] += 1
    for k in range(len(between)):
        if between[k] > 2:
            between[k] = 0 
            between[k+1] += 1 
    e = ""
    for j in numbers:
        e += str(j)
        if j != 9:
            e += operators[between[j-1]]
   
    if eval(e) == target:
        print(e)
    