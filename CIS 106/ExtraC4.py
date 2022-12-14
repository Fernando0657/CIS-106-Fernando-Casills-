line = input("Please enter a line of text: ")

num_chars = int(input("Please enter the number of characters per line: "))
num_lines = int(input("Please enter the number of lines to be printed: "))

 
scroll_dir = input("Please enter the scroll direction (right or left): ")

line = line * (num_chars // len(line) + 1)

for i in range(num_lines):
    print(line)

    if scroll_dir == "right":
        line = line[-1] + line[:-1]
    elif scroll_dir == "left":
        line = line[1:] + line[0]
