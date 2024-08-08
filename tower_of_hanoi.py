def tower(n,a,b,c):
    if n==1: #if only one disk is left in the tower a the it will be tranfered to c
        print(f"move 1st disk from {a} to {c}")
        return
    tower(n-1,a,c,b) #the disk in a transfers to b woth the help of c
    print(f"move {n}th disk from {a} to {c}") #when the disk form a are tranfered to b via c then the last disk at a is trnafer to c
    tower(n-1,b,a,c) # now the disks at b are tanfered to c via a (uses the above recurtion to get the the n-1 disk to again b)



a = int(input("enter the number of disk "))
tower(a, "A" , "B" , "C")


