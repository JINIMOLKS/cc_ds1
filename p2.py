list=[1,3]
while True:
    print("\n1)Add 2)view 3)Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        it=input("Enter list: ").strip()
        if it:
         list.append(it)
         print("Added:",it)
        else:
            print("empty input ignored.")
    elif choice==2:
        if not list:
            print("Inventory is empty")
        else:
            for i,it in enumerate(list,start=1):
                print(i,it)
    elif choice==3:
        print("Exiting")
        break
    else:
        print("invalid choice,please enter a valid choice")

