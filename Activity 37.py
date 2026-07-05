def print_mirrored_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(i):
            print("*", end="")
        print() # Move to the next line

# Test the function with 5 rows
print_mirrored_triangle(5)