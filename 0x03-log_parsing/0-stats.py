#!/usr/bin/python3
'''
'''

import sys


def printOutput(stats, filesize):
  print("File size: {:d}".format(filesize))
  for k, v in stats.items:
    print("{}: {}".format(k, v))


if __name__ == '__main__':
  possible_status = ["200", "301", "400", "401", "403", "404", "405", "500"]
  file_size, count = 0, 0
  stats = {stat: 0 for stat in possible_status}


  try:
    for line in sys.stdin:
      count += 1
      data = line.split()
      try:
        read_status = data[-2]
        if read_status in stats:
          stats[read_status] += 1
      except BaseException:
        pass
      try:
        file_size += int(data[-1])
      except BaseException:
        pass
      if count % 10 == 0:
        printOutput(stats, file_size)
    printOutput(stats, file_size)
  except KeyboardInterrupt:
        printOutput(stats, file_size)