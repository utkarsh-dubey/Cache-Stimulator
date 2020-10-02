
#Made by- Utkarsh Dubey
#Roll no- 2019213
#section- A
#Group- 7






from time import sleep
from math import log

def direct():

    cache=[]
    datacache=[]

    # print("\n")
    print("Enter the size of cache")
    s=int(input())
    print("Enter the number of lines in cache")
    lines=int(input())
    linepower=int(log(lines,2))

    block=s//lines
    blockpower=int(log(block,2))



    for i in range(lines):
        cache.append(-1)
    for i in range(lines):
        temp=[]
        for j in range(block):
            temp.append(-1)
        datacache.append(temp)

    # print(datacache)


    # print("\n")
    while(True):
        print()
        print("Choose what you want to do-")
        print("1- Read from the cache")
        print("2- Write into cache")
        print("3- Leave current type of Mapping")
        print("press the corresponding number in order to continue....")

        choice=int(input())
        address="0"
        data="0"
        if(choice==1):
            # print()
            print("Enter the address")
            address=str(input())
            linenumber=int(address[-(blockpower+linepower):-blockpower],2)
            tag=int(address[0:-(blockpower+linepower)],2)
            offset=(int(address[-(blockpower):],2))

            if(cache[linenumber]==tag):
                print("Read hit")
                print("The data present at the given address-",end=" ")
                # sleep(1)
                print(datacache[linenumber][offset])
                # sleep(2)
            else:
                print("Read miss")
                print("Given address not present in the cache")
                # sleep(2)
                linenumber = int(address[-(blockpower + linepower):-blockpower], 2)
                tag = int(address[0:-(blockpower + linepower)], 2)
                offset = (int(address[-(blockpower):], 2))
                if (cache[linenumber] != -1 and cache[linenumber] == tag):
                    # print("We are replacing the previous entry with this new entry")
                    # print("write hit")
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                else:
                    # print("No replacement was needed....putting your data..")
                    # print("replacing the already present")
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)



        elif(choice==2):
            # print()
            print("Enter the address")
            address=str(input())
            print("Enter the data")
            data=str(input())
            linenumber = int(address[-(blockpower + linepower):-blockpower], 2)
            tag = int(address[0:-(blockpower + linepower)], 2)
            offset = (int(address[-(blockpower):], 2))
            if(cache[linenumber]==-1 and cache[linenumber]==tag):
                # print("We are replacing the previous entry with this new entry")
                print("write hit")
                cache[linenumber]=tag
                datacache[linenumber][offset]=data
                # sleep(1)
            else:
                # print("No replacement was needed....putting your data..")
                if(cache[linenumber]!=-1):
                    print("Line is already occupied")
                    print("Replacing the data")
                else:
                    print("write miss")
                cache[linenumber]=tag
                datacache[linenumber][offset]=data
                # sleep(1)


        elif(choice==3):
            break
        else:
            print("great you pressed something wrong...")
            sleep(2)
            print("cool then....")
            sleep(2)
            print("exiting....")
            sleep(2)
            print("next time be serious while using this....")
            sleep(2)
            print("k bye...")
            sleep(2)
            exit(0)

    flag=0
    print("Do you want to use other types of mapping?(y/n)")
    check=str(input())
    if(check.lower()=='y'):
        flag=1
    else:
        flag=0

    return flag







def associative():

    cache = []
    datacache = []

    # print("\n")
    print("Enter the size of cache")
    s = int(input())
    print("Enter the number of lines in cache")
    lines = int(input())


    number = lines
    setpower = int(log(lines // number, 2))


    block = s // lines
    blockpower = int(log(block, 2))

    for i in range(lines):
        cache.append(-1)
    for i in range(lines):
        temp = []
        for j in range(block):
            temp.append(-1)
        datacache.append(temp)

    # print(datacache)
    lcr = []
    for i in range(lines):
        lcr.append(-1)
    # print("\n")
    current = 0
    while (True):
        print()
        current += 1
        print("Choose what you want to do-")
        print("1- Read from the cache")
        print("2- Write into cache")
        print("3- Leave current type of Mapping")
        print("press the corresponding number in order to continue....")
        # print(cache)
        # print(datacache)
        choice = int(input())
        address = "0"
        data = "0"
        if (choice == 1):
            # print()
            print("Enter the address")
            address = str(input())

            setnumber = 0

            tag = int(address[0:-(blockpower + setpower)], 2)
            offset = (int(address[-(blockpower):], 2))

            if tag in cache[setnumber * number:(setnumber + 1) * number]:
                print("Read hit")
                # sleep(1)
                linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(tag)
                linenumber = setnumber * number + linenumbertemp
                lcr[linenumber] = current
                print("The data present at the given address-",end=" ")
                print(datacache[linenumber][offset])
                # sleep(2)
            else:
                print("Read miss")
                print("Given address not present in the cache")

                setnumber = 0

                tag = int(address[0:-(blockpower + setpower)], 2)
                offset = (int(address[-(blockpower):], 2))

                # number = lines // k
                if tag in cache[setnumber * number:(setnumber + 1) * number]:

                    # print("Write hit")
                    linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(tag)
                    linenumber = setnumber * number + linenumbertemp
                    # print("writing in set: " + str(setnumber) + " and in line: " + str(linenumber))

                    lcr[linenumber] = current
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                elif (cache[setnumber * number:(setnumber + 1) * number].count(-1) != 0):
                    # print("Write hit")
                    linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(-1)
                    linenumber = setnumber * number + linenumbertemp
                    # print("writing in set: " + str(setnumber) + " and in line: " + str(linenumber))
                    lcr[linenumber] = current
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                else:
                    # print("Required set is full hence removing the block using LRU")
                    minimum = min(lcr[setnumber * number:(setnumber + 1) * number])
                    linenumbertemp = lcr[setnumber * number:(setnumber + 1) * number].index(minimum)
                    linenumber = setnumber * number + linenumbertemp
                    # print("Line " + str(linenumber) + " is being replaced")
                    lcr[linenumber] = current
                    # linenumber=cache[setnumber * number:(setnumber + 1) * number].index(-1)
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                # sleep(2)



        elif (choice == 2):
            # print()
            print("Enter the address")
            address = str(input())
            print("Enter the data")
            data = str(input())

            setnumber = 0

            tag = int(address[0:-(blockpower + setpower)], 2)
            offset = (int(address[-(blockpower):], 2))

            # number = lines // k
            if tag in cache[setnumber * number:(setnumber + 1) * number]:

                print("Write hit")
                linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(tag)
                linenumber = setnumber * number + linenumbertemp
                print("writing in line: " + str(linenumber))

                lcr[linenumber] = current
                cache[linenumber] = tag
                datacache[linenumber][offset] = data
                # sleep(1)
            elif (cache[setnumber * number:(setnumber + 1) * number].count(-1) != 0):
                print("write miss")
                linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(-1)
                linenumber = setnumber * number + linenumbertemp
                print("writing in line: " + str(linenumber))
                lcr[linenumber] = current
                cache[linenumber] = tag
                datacache[linenumber][offset] = data
                # sleep(1)
            else:
                print("Cache is full hence removing the block using LRU")
                minimum = min(lcr[setnumber * number:(setnumber + 1) * number])
                linenumbertemp = lcr[setnumber * number:(setnumber + 1) * number].index(minimum)
                linenumber = setnumber * number + linenumbertemp
                print("Line " + str(linenumber) + " is being replaced")
                # linenumber=cache[setnumber * number:(setnumber + 1) * number].index(-1)
                lcr[linenumber] = current
                cache[linenumber] = tag
                datacache[linenumber][offset] = data
                # sleep(1)


        elif (choice == 3):
            break
        else:
            print("great you pressed something wrong...")
            sleep(2)
            print("cool then....")
            sleep(2)
            print("exiting....")
            sleep(2)
            print("next time be serious while using this....")
            sleep(2)
            print("k bye...")
            sleep(2)
            exit(0)

    flag = 0
    print("Do you want to use other types of mapping?(y/n)")
    check = str(input())
    if (check.lower() == 'y'):
        flag = 1
    else:
        flag = 0

    return flag





def nway(k=0):

    cache=[]
    datacache = []

    # print("\n")
    print("Enter the size of cache")
    s = int(input())
    print("Enter the number of lines in cache")
    lines = int(input())

    if(k==0):
        number=lines
        setpower=int(log(lines//number,2))
    else:
        number = k
        setpower = int(log(lines//number, 2))


    block = s // lines
    blockpower = int(log(block, 2))

    for i in range(lines):
        cache.append(-1)
    for i in range(lines):
        temp = []
        for j in range(block):
            temp.append(-1)
        datacache.append(temp)

    # print(datacache)
    lcr=[]
    for i in range(lines):
        lcr.append(-1)
    # print("\n")
    current=0
    while (True):
        print()
        current+=1
        print("Choose what you want to do-")
        print("1- Read from the cache")
        print("2- Write into cache")
        print("3- Leave current type of Mapping")
        print("press the corresponding number in order to continue....")
        # print(cache)
        # print(datacache)
        choice = int(input())
        address = "0"
        data = "0"
        if (choice == 1):
            # print()
            print("Enter the address")
            address = str(input())
            if(k==0):
                setnumber=0
            else:
                setnumber = int(address[-(blockpower + setpower):-blockpower], 2)
            tag = int(address[0:-(blockpower + setpower)], 2)
            offset = (int(address[-(blockpower):], 2))

            if tag in cache[setnumber*number:(setnumber+1)*number]:
                print("Read hit")
                # sleep(1)
                linenumbertemp=cache[setnumber*number:(setnumber+1)*number].index(tag)
                linenumber=setnumber*number+linenumbertemp
                lcr[linenumber]=current
                print("The data present at the given address-",end=" ")
                print(datacache[linenumber][offset])
                # sleep(2)
            else:
                print("Read miss")
                print("Given address not present in the cache")
                # if (k == 1):
                #     setnumber = 0
                # else:
                setnumber = int(address[-(blockpower + setpower):-blockpower], 2)
                tag = int(address[0:-(blockpower + setpower)], 2)
                offset = (int(address[-(blockpower):], 2))

                # number = lines // k
                if tag in cache[setnumber * number:(setnumber + 1) * number]:

                    # print("Write hit")
                    linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(tag)
                    linenumber = setnumber * number + linenumbertemp
                    # print("writing in set: " + str(setnumber) + " and in line: " + str(linenumber))

                    lcr[linenumber] = current
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                elif (cache[setnumber * number:(setnumber + 1) * number].count(-1) != 0):
                    # print("Write hit")
                    linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(-1)
                    linenumber = setnumber * number + linenumbertemp
                    # print("writing in set: " + str(setnumber) + " and in line: " + str(linenumber))
                    lcr[linenumber] = current
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                else:
                    # print("Required set is full hence removing the block using LRU")
                    minimum = min(lcr[setnumber * number:(setnumber + 1) * number])
                    linenumbertemp = lcr[setnumber * number:(setnumber + 1) * number].index(minimum)
                    linenumber = setnumber * number + linenumbertemp
                    # print("Line " + str(linenumber) + " is being replaced")
                    lcr[linenumber]=current
                    # linenumber=cache[setnumber * number:(setnumber + 1) * number].index(-1)
                    cache[linenumber] = tag
                    datacache[linenumber][offset] = -1
                    # sleep(1)
                # sleep(2)



        elif (choice == 2):
            # print()
            print("Enter the address")
            address = str(input())
            print("Enter the data")
            data = str(input())
            if(k==0):
                setnumber=0
            else:
                setnumber = int(address[-(blockpower + setpower):-blockpower], 2)
            tag = int(address[0:-(blockpower + setpower)], 2)
            offset = (int(address[-(blockpower):], 2))

            # number = lines // k
            if tag in cache[setnumber*number:(setnumber+1)*number]:

                print("Write hit")
                linenumbertemp = cache[setnumber * number:(setnumber + 1) * number].index(tag)
                linenumber = setnumber * number + linenumbertemp
                print("writing in set: "+str(setnumber)+" and in line: "+str(linenumber))

                lcr[linenumber] = current
                cache[linenumber] = tag
                datacache[linenumber][offset] = data
                # sleep(1)
            elif(cache[setnumber * number:(setnumber + 1) * number].count(-1)!=0):
                print("write miss")
                linenumbertemp=cache[setnumber * number:(setnumber + 1) * number].index(-1)
                linenumber=setnumber * number+linenumbertemp
                print("writing in set: "+str(setnumber)+" and in line: "+str(linenumber))
                lcr[linenumber] = current
                cache[linenumber] = tag
                datacache[linenumber][offset] = data
                # sleep(1)
            else:
                print("Required set is full hence removing the block using LRU")
                minimum=min(lcr[setnumber * number:(setnumber + 1) * number])
                linenumbertemp=lcr[setnumber * number:(setnumber + 1) * number].index(minimum)
                linenumber = setnumber * number + linenumbertemp
                print("Line "+str(linenumber)+" is being replaced")
                # linenumber=cache[setnumber * number:(setnumber + 1) * number].index(-1)
                lcr[linenumber]=current
                cache[linenumber] = tag
                datacache[linenumber][offset] = data
                # sleep(1)


        elif (choice == 3):
            break
        else:
            print("great you pressed something wrong...")
            sleep(2)
            print("cool then....")
            sleep(2)
            print("exiting....")
            sleep(2)
            print("next time be serious while using this....")
            sleep(2)
            print("k bye...")
            sleep(2)
            exit(0)









    flag = 0
    print("Do you want to use other types of mapping?(y/n)")
    check = str(input())
    if (check.lower() == 'y'):
        flag = 1
    else:
        flag = 0

    return flag






if __name__ == '__main__':

    flag=1
    while(flag==1):

        print("Welcome to the cache stimulation program")
        print()
        print("Choose the type of mapping you want to work with")
        print("1- Direct Mapping")
        print("2- Associative Memory")
        print("3- n-way set Associative Memory")
        print("press the corresponding number in order to continue")
        choice=int(input())
        flag=0
        if(choice==1):
            flag=direct()
        elif(choice==2):
            flag=associative()
        elif(choice==3):
            print("Enter the value of n")
            k=int(input())
            flag=nway(k)
        else:
            print("great you pressed something wrong...")
            sleep(2)
            print("cool then....")
            sleep(2)
            print("exiting....")
            sleep(2)
            print("next time be serious while using this....")
            sleep(2)
            print("k bye...")
            sleep(2)
            exit(0)

    print("Thank you for using my stimulation")
