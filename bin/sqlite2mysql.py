#!/usr/bin/env python

import re, fileinput

def main():
  for line in fileinput.input():
    process = False
    for nope in ('BEGIN TRANSACTION','COMMIT',
                 'sqlite_sequence','CREATE UNIQUE INDEX'):
      if nope in line: break
    else:
      process = True
    if not process: continue
    m = re.search('INSERT INTO "([a-z_]*)"(.*)', line)
    if m:
      line = 'INSERT INTO %s%s\n' % m.groups()
      line = line.replace('"', r'\"')
      line = line.replace('"', "'")
    else:
      line = line.replace('"', '`')
    line = re.sub(r"([^'])'t'(.)", "\1THIS_IS_TRUE\2", line)
    line = line.replace('THIS_IS_TRUE', '1')
    line = re.sub(r"([^'])'f'(.)", "\1THIS_IS_FALSE\2", line)
    line = line.replace('THIS_IS_FALSE', '0')
    print line,

main()
