list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

x = "hel"
for k in x:
    print(k)
    print("hi")
    print("yes")

table = [10, 20, 50, 100, 500]
inhand = 0
for x in table:
    if x > inhand:
        inhand = x
print(inhand)


table = [10, 20, 50, 100, 500, 600]
inhand = 0
for x in table:
    inhand = x + inhand  # first it take 10 as inhand then loop continuous (10+20+50+100+500+600)
print(inhand)

A = "Hi hello, how are you , how are your friends , our friend are good"
find = "our"
repl = "OUR"
z = " "
for k in A.split():
    if k == find:
        print(repl, end="")
        z = z + " " + repl
    else:
        print(k,end="")
        z= z + " " + k
print(z)



totalseats = {1, 2, 3, 4, 5, 6, 7, 8}
bookedseats= {2, 3, 7}
z = int(input("enter seats: "))
for z in totalseats:
    if z not in bookedseats:
        a = bookedseats.add(z)
        bookedseats.remove(z)
        print(a)
        print("seat added")
        break
    else:
        print(bookedseats)

