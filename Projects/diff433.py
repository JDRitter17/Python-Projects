def fileinstructions(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Compare lines that exist in both files
    for line1, line2 in zip(lines1, lines2):
        line1_clean = line1.rstrip()
        line2_clean = line2.rstrip()
        if line1_clean == line2_clean:
            print(f"Lines '{line1_clean}' and '{line2_clean}' are equal.")
        else:
            print(f"Change line to say '{line2_clean}'")

    # Handle any additional lines in file2 beyond length of file1
    for line in lines2[len(lines1):]:
        print(f"Add line that says '{line.rstrip()}'")

file1 = r"C:\Users\jritter\Desktop\f1.txt"
file2 = r"C:\Users\jritter\Desktop\f2.txt"
fileinstructions(file1, file2)
