# fix-subXids
Generates sorted and non-overlapping subXid lines from your /etc/passwd file

Python program to iterate your /etc/passwd file and use the first file (username)
to generate a sorted list to stdout of the lines for /etc/subuid and /etc/subgid
with non-overlapping IDs

Use for Podman-Rootless
Note you will need entry for _apt to use apt update inside the Container

March 2022

