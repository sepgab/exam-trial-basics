def count_as(file_name):
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.
    try:
        f = open(file_name, 'r')
        file_content = f.read()
        a_counter = 0
        for letter in file_content:
            if letter == 'a' or letter == 'A':
                a_counter += 1
        f.close()
        return a_counter
    except FileNotFoundError:
        return 0

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
