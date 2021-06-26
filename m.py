matrix1=[]
print("****Enter values for Matrix1****")
m1=int(input("enter how many rows"))
n1=int(input("enter how many columns"))
for i in range(m1):
    row1=[]
    for j in range(n1):
        value1=int(input("enter value"))
        row1.append(value1)
    matrix1.append(row1)
for row1 in matrix1:
    for col1 in row1:
        print(col1,end=' ')
    print()
matrix2=[]
print("****Enter values for Matrix2****")
m2=int(input("enter how many rows"))
n2 =int(input("enter how many columns"))
for i in range(m2):
    row2=[]
    for j in range(n2):
        value2=int(input("enter value"))
        row2.append(value2)
    matrix2.append(row2)
for row2 in matrix2:
    for col2 in row2:
        print(col2,end=' ')
    print()
print()
if(n1==m2):
    matrix3=[]
    for i in range(m1):
        row3=[]
        for j in range(n2):
            value3=0
            row3.append(value3)
        matrix3.append(row3)
    for i in range(m1):
        for j in range(n2):
            for k in range(m2):
                matrix3[i][j]+=matrix1[i][k]*matrix2[k][j]
    for row3 in matrix3:
        for col3 in row3:
            print(col3,end=' ')
        print()
else:
    print("Multiplication not possible")

