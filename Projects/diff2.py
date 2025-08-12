def fileinstructions(file1, file2):
    count = 0
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for i in range(max(len(lines1), len(lines2))):
        if i < len(lines1) and i < len(lines2):
            if lines1[i].rstrip() == lines2[i].rstrip():
                print("lines Match. Move to next line")
            elif lines1[i].rstrip() == lines2[i-1].rstrip() and count > 0:
                print("Lines match. Move to next lines")
                count -= 1
                if count == 0:
                    print(f"Delete line: {lines2[i].rstrip()}")
            else:
                print(f"Insert line: {lines1[i].rstrip()}")
                count += 1 + i

file1 = "C:\\Users\\jritter\\Desktop\\f1.txt"
file2 = "C:\\Users\\jritter\\Desktop\\f2.txt"
fileinstructions(file1, file2)