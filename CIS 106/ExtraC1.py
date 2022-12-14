name = input("Please enter your first and last name: ")

parts = name.split()

if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]

    formatted_name = last_name + ", " + first_name[0] + "."

    print(formatted_name)
else:
    print("Invalid name! Please enter your first and last name.")
