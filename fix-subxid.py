#!/usr/bin/env python3


__version__ = '0.0.1'

if __name__ == "__main__":

  #filename = "/etc/subuid"
  accounts = "/etc/passwd"
  users = []

  try:
    with open(accounts) as f:
        contents = f.readlines()
    for line in contents:
        line_list = line.rstrip().split(':')
        users.append(line_list[0])
  except FileNotFoundError:
        print('ERROR: File not found.')
        exit(1)
  finally:
        print('Found %d accounts' % len(users))

  users = sorted(users)
  start1 = 10000
  step1 = start1

  for user in users:
    str1 = "{}:{}:65536".format(user, step1, step1 * 65536)
    print(str1)
    step1 = step1+65536

exit(0)
