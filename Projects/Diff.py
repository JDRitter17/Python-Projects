def compare_files_add(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = [line.rstrip() for line in f1]
        file2_lines = [line.rstrip() for line in f2]

    addfile = [line for line in file1_lines if line not in file2_lines]

    print(f"Add: {addfile}")


def compare_files_delete(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = [line.rstrip() for line in f1]
        file2_lines = [line.rstrip() for line in f2]

    deletefile = [line for line in file2_lines if line not in file1_lines]

    print(f"Delete: {deletefile}")


file1 = r"C:\Users\jritter\Desktop\f1.txt"
file2 = r"C:\Users\jritter\Desktop\f2.txt"

compare_files_delete(file1, file2)
compare_files_add(file1, file2)
