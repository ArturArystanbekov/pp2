def write_list(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for i in data:
                file.write(str(i) + '\n')
        print("List has been written to the file successfully")
    except IOError:
        print("An error occurred while writing to the file")
        
        
liss = ["apple", "banan", "cherry"]

file_path = "file.txt"

write_list(file_path, liss)