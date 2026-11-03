# Student Details Program

name = input("Enter Student Name: ")
usn = input("Enter Student USN: ")

mark1 = float(input("Enter Subject 1 Marks: "))
mark2 = float(input("Enter Subject 2 Marks: "))
mark3 = float(input("Enter Subject 3 Marks: "))

average = (mark1 + mark2 + mark3) / 3

print("\n--- Student Details ---")
print("Name:", name)
print("USN:", usn)
print("Average Marks:", average)
