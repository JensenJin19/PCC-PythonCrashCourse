filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line)

'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()  # read 到达文件末尾时返回一个空字符串

print(contents.rstrip())  # delete empty line

'''