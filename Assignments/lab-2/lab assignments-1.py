lst = list(map(int, input("Enter list elements: ").split()))
key = int(input("Enter number to search: "))

found = False
for i in range(len(lst)):
    if lst[i] == key:
        print("Element found at position:", i)
        found = True
        break

if not found:
    print("Element not found")