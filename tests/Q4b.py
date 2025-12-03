fil = input("please enter the name of a file to open: ")
try:
    open(fil, "r")
except Exception as _:
    print(f"the file \"{fil}\" does not exist. exiting.")
    exit()

print("Continue with rest of program")
