#module starts
import time
name=input("What is Your Name \n: ")
print(f"\nHello {name} , Welcome To Oxy PY Project")
time.sleep(1)
xa = time.localtime()

while True:
    j= input("\nWhat Name and Type of file you want to create?\n Example myname, myname.extension\n @oxyop-op ")
    time.sleep(1)
    x = input("\nWhat is content of your file:\n @oxyop-op ")
    try:
        file = open(j,"x")
        file.write(x)
        file.close()
        print("\nDone")
    except (FileNotFoundError):
        print("\nError404 File Not Found Or Please Give a Name To Your File")
    except (FileExistsError):
        print("\nError: File Name Already Exists Try Deleting Or Create a new file with differant name")
    except OSError:
        print("Error")
    except (ValueError, TypeError):
        print("Value or Type Error")
        break

