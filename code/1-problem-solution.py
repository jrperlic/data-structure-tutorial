shelf = input()
stack = []

for item in shelf:
    if item == "[":
        stack.append(item)
    elif item == "]":
        if len(stack) == 0 or stack.pop() != "[":
            print("False")
            exit()
    elif item == "|":
        continue
    else:
        print("False")
        exit()
print("True")