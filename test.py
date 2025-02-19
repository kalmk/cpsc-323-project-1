keywords = ["int"]

def scan_line():
    file = open("input.in", "r")
    lines = file.readlines()

    dummy = []


    for i in lines[0]:
        dummy.append(i)

        if i == " ":
            dummy.pop()

        print(f"Dummy current: {dummy}")

        # if newline, we can use it for comments

        if ''.join(dummy) in keywords:
            print("a keyword!")
            dummy.clear()


