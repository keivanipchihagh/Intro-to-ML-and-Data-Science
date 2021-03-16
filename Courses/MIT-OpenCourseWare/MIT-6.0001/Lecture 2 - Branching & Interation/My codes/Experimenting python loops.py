hi = "hi"
name = "ana"
greet = hi + name  
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name)*3
print(silly)

x = 1
x_str = str(x)
print("my fav number is", x, ".", "x = ", x)
print("my fav number is", x_str + "." + "x = " + x_str)
print("my fav number is" + x_str + "." + "x = " + x_str)

text = input("Type anything... ")
print(5*text)
num = int(input("Type a number... "))
print(5*num)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

for n in range(5):
    print(n)

mysum = 0
for i in range(10):
    mysum += i
print(mysum)

mysum = 0
for i in range(7, 25):
    mysum += i
print(mysum)

mysum = 0
for i in range(0, 18, 2):
    mysum += i
    if mysum == 7:
        break
        mysum += 1
print(mysum)

# Perfect Sequence
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")
