# Python program to transform Ascii text into C/C++ console text
# Generate text in https://patorjk.com/software/taag/ and paste it in asciiInput.txt
# The result will be saved in asciiOutput.txt

asciiInput = open("asciiInput.txt", "r")
asciiOutput = open("asciiOutput.txt", "w")

lines = asciiInput.readlines()

print("1: C, 2: C++\n")
op = input("Wich language export to? --> ")
op = int(op)

while op != 1 and op != 2:
    print("\nFailed, try again. ")
    op = input("Wich language export to? --> ")
    op = int(op)

for line in lines:
    if op == 1:
        code = "printf(\""
    else:
        code = "cout<<\""

    actualLine = ""
    actualLine += line

    finalLine = actualLine.replace("\\", "\\\\")

    position = finalLine.find('\n')

    for i in range(position):
        code += finalLine[i]

    code += "\\n"
    code += "\""

    if op == 1:
        code += ")"

    code += ";"

    asciiOutput.write(code)
    asciiOutput.write('\n')

asciiInput.close()
asciiOutput.close()

print("\nFile created succesfully.")
