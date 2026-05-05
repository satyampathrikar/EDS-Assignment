marks = list(map(int, input("Enter marks: ").split()))

total = sum(marks)
percentage = total / len(marks)

print("Total Marks:", total)
print("Percentage:", percentage)