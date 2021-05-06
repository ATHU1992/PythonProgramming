def split_and_join(line):
    line_list = line.split()
    line = "-".join(line_list)
    return line


line1 = "this is a string"
result = split_and_join(line1)
print(result)
