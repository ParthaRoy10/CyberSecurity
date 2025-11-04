# <!-- dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr -->

## Level 11:

### Level Goal

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

### Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

### Helpful Reading Material

Rot13 on Wikipedia


### Solution:

The password is encoded in ROT 13 encryption 

```
cat data.txt | tr [n-za-mN-ZA-M] [a-zA-Z]
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
<!-- 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4 -->

## Level 12 :

### Level Goal :

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

#### Commands you may need to solve this level

`grep`, `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `bzip2`, `xxd`, `mkdir`, `cp`, `mv`, `file`

#### Helpful Reading Material

Hex dump on Wikipedia

### Solution :

The flag here is set  as hexdump file .

## Level 13 :


