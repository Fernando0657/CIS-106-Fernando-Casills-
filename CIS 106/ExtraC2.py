line = input("Please enter a line of text: ")

line = line.strip()

line = " ".join(line.split())

print(line[::-1])
