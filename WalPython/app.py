from customer import Customer
import csv
import numpy
import json

def promptRow():
    return(int(input("Please enter the number of row: ")))

def promptCol():
    return(int(input("Please enter the number of column: ")))

def promptFName():
    return(input("Please enter the file name: "))

def promptCName():
    return(input("Please enter the customer list name: "))

def menu():
    print("B = buy ticket for customer")
    print("C = check customers list")
    print("S = check available seat")
    print("N = New Seat Plan")
    print("R = Read Old Plan")
    print("W = Save Seat Plan to csv file")
    print("M = menu")
    print("Q = quit")


def handleTicket(seat, customer, row, col):
    cd = "Y"
    while (cd == "Y" or cd == "y"):
        rowT = promptRow()
        colT = promptCol()
        if (rowT < 0  or rowT > row):
            print("Row Out of range")
            okR = False
        else:
            okR = True

        if (colT < 0  or colT > col):
            print("Column Out of range")
            okC = False
        else:
            okC = True

        if okR == True and okC == True:
            if (seat[rowT - 1][colT - 1] != 1):
                customer.reserve.append([rowT, colT])
                seat[rowT - 1][colT - 1] = 1
                cd = input("Do you wanna buy more ticket? Y / N")
            else:
                print("Seat not available")

def writeCSV(seat, name):
    with open("{}.csv".format(name).format(), "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(seat)

def writeJson(customerList, nameC):
    # with open('{}.txt'.format(nameC), 'w') as file:
    #     json.dump(customerList.__dict__, file)
    pass



def readCSV(name, seat):
    datafile = open('{}.csv'.format(name), 'r')
    datareader = csv.reader(datafile, delimiter=',', quotechar = '"')
    #how to read it as a 2d int array?
    for row in datareader:
        seat.append(row)


def main():
    #instruction
    seat = []
    customerList = []
    availiableS = -1
    row = -1
    col = -1
    menu()
    command = input("Please enter a command: ")
    while (command.lower() != "q"):
        if (command == "R" or command == "r"):
            name = promptFName()
            readCSV(name, seat)
            availiableS = sum(x.count('0') for x in seat)
            row = len(seat)
            col = len(seat[0])

        elif (command == "W" or command == "w"):
            name = promptFName()
            nameC = promptCName()
            writeCSV(seat, name)
            writeJson(customerList, nameC)

        elif (command == "N" or command == "n"):
            row = promptRow()
            col = promptCol()
            availiableS = row * col
            customerList = []
            # initialize all to 0 mark as available
            seat = [[0 for x in range(col)] for x in range(row)]

        elif ((command == "B" or command == "b") and len(seat)!=0):
            name = input("Customer name: ")
            age = int(input("Customer age: "))
            customer = Customer(name, age)
            handleTicket(seat, customer, row, col)
            availiableS -= 1
            customerList.append(customer)

        elif (command == "C" or command == "c"):
            for c in customerList:
                c.display()

        elif (command == "S" or command == "s"):
            print("There are {} available seat.".format(availiableS))
            print("The Seat Map:")
            for i in seat:
                print (i)

        elif (command == "M" or command == "m"):
            menu()

        else:
            print("Unknown command! / Empty data set!")
        print()
        print()
        menu()
        command = input("Please input a command: ")
    print("Goodbye")

if __name__ == '__main__':
    main()