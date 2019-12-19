with open("numbers.txt", "w") as writer:
    # Write even numbers from 0 to 30
    for num in range(0, 31):
        if num % 2 == 0:
            writer.write(f"{num}\n")

# Copy contents of one file to another
with open("read.txt") as reader:
    with open("copy.txt") as copy:
        copy.write(reader.read())