######################################################################
#
# Function Name:    Square
# Input:            Integer Number
# Description:      Return the Square value of number 
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def CheckGreater(Value1, Value2):

    if (Value1 > Value2):
        return Value1

    else:
        return Value2

######################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes user Input and Calls the Square Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def main():
    No1 = int(input("Enter First Number:-"))
    No2 = int(input("Enter Second Number:-"))

    Ans = CheckGreater(No1, No2)

    print("Greater number is:-",Ans)

######################################################################
#
# Starter of the Main Function
#
######################################################################

if __name__ == "__main__":
    main()