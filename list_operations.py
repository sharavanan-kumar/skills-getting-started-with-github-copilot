def process_list_commands():
    # Initialize empty list
    my_list = []
    
    # Read number of commands
    n = int(input())
    
    # Process each command
    for _ in range(n):
        command = input().split()
        
        if command[0] == "insert":
            i = int(command[1])  # position
            e = int(command[2])  # element
            my_list.insert(i, e)
            
        elif command[0] == "print":
            print(my_list)
            
        elif command[0] == "remove":
            e = int(command[1])  # element to remove
            my_list.remove(e)
            
        elif command[0] == "append":
            e = int(command[1])  # element to append
            my_list.append(e)
            
        elif command[0] == "sort":
            my_list.sort()
            
        elif command[0] == "pop":
            my_list.pop()
            
        elif command[0] == "reverse":
            my_list.reverse()

if __name__ == "__main__":
    process_list_commands()
