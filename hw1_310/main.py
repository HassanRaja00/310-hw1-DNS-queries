from mydig import MyDig  # this is a custom class that I made as an object
import dns.resolver

if __name__ == "__main__":
    # taking input for address to be dug up
    addr = input("Enter address: ")
    digObj = MyDig(addr)
    try:
        digObj.getOutput()
    except:
        print("query failed")


    

