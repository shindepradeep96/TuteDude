var_1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as text_file:
    output1 = text_file.write(var_1+'\n')
    print("Data successfully written to output.txt")
var_2 = input("Enter additional text to append: ")
with open("output.txt", "a") as text_file:
    output2 = text_file.write(var_2)
    print("Data successfully appended")
with open("output.txt", "r") as text_file:
    output3 = text_file.read()
    print("Final content of output.txt:\n",output3)