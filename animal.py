import sys

def default():
    print ("Hello")

def cat():
    print("miavvv")

def main():
    if sys.argv[1]=='cat':
        cat()
    else:
        default()

if __name__=="__main__":
    main()

