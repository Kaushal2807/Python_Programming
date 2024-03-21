# f = open("04_iternations/file.py")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())



# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# for line in open('04_iternations/file.py'):
#     print(line,end='')

# while True:
#     line = f.readline()
#     if not line: break
#     print(line,end='')

test = "ABC"
if not test:
    print("Hello")  # No output

test = ""
if not test:
    print("Hello")

myList = [1,2,3,4]
I = iter(myList)
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

f = open('04_iternations/file.py')
bool = iter(f) is f 
print(bool)

myNewList = [1,2,3]
bool1 = iter(myNewList) is myNewList
print(bool1)

dic = {'a':1,'b':2,'c':3}
for key in dic.keys():
    print(key)

D = {'a':1,'b':2}
I =  iter(D)
print(next(I))
print(next(I))


a = range(5)
print(a)
R = range(5)
I = iter(R)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
