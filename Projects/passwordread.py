with open(r"C:\Users\jritter\Desktop\passwd.txt", "r") as f:
    root_users = []
    count = 0
    homedirs = []
    multihomedirs = set()
    dif_id = []

    for line in f:
        data = line.strip().split(":")

        user = data[0]
        uid = int(data[2])
        gid = int(data[3])
        homedir = data[5]
        shell = data[6]

        # Users with UID 0 (root)
        if uid == 0:
            root_users.append(user)

        # Count users with /bin/bash shell and UID > 999 or UID 0
        if shell == "/bin/bash" and (uid > 999 or uid == 0):
            count += 1

        # Users where UID and GID differ
        if uid != gid:
            dif_id.append(user)

        # Check for multiple users with the same home directory
        if homedir in homedirs:
            multihomedirs.add(homedir)
        homedirs.append(homedir)

print(f"Users with root permissions: {root_users}")
print(f"Number of users with /bin/bash and UID > 999 or 0: {count}")
print(f"Home directories used by multiple users: {list(multihomedirs)}")
print(f"Users whose group ID differs from user ID: {dif_id}")
