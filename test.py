keywords = ["int", "main"]
unique = ["(", ")"]

def scan_line():
    file = open("input.in", "r")
    lines = file.readlines()

    dummy = []


    for i in lines[0]:
        dummy.append(i)

        print(f"Dummy current: {dummy}")

        if i == " ":
            dummy.pop()

        if i in unique:
            print("A unique!")
            dummy.clear()

        if i == '\n':
            print("Newline!")
            dummy.clear()

        # if newline, we can use it for comments

        if ''.join(dummy) in keywords:
            print("a keyword!")
            dummy.clear()

        


