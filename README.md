# fix-subXids
Generates sorted and non-overlapping subXid lines from your /etc/passwd file.

Python program to iterate your /etc/passwd file and use the first field (username)
to generate a sorted list to stdout of the lines for /etc/subuid and /etc/subgid
with non-overlapping IDs.

Use for Podman-Rootless

I.E: you will need entry for _apt so you can use apt update inside the Container

March 2022

