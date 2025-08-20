try:
    
    filename = input("Enter the filename you want to read: ")

    with open(filename, "r") as infile:
        content = infile.read()
        print("File read successfully!")

    modified_content = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("Modified content has been written to output.txt")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the name and try again.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
