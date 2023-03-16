a=int(input("Введите 1 число"))
b=int(input("Введите 2 число"))
c=int(input("Введите 3 число"))
sum=0
for i in a, b, c:
    sum=((i+1)//2)+sum
print(sum)