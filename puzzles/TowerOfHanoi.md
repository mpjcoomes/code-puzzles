# Tower of Hanoi

This is a puzzle created by Edouard Lucas in 1883. It involves 3 rods with a number of disks of differing size. The puzzle starts with all disks on 1 rod, ordered by size, with the largest disk at the base. It thus resembles a pagoda, where each ascending tier of a tower is smaller than the tier below it. 

![](figures/BaoblazeToH.jpg "10 Ring Tower of Hanoi, courtesy of Baoblaze.")

The goal is to move all disks from 1 rod to another under the following restrictions:

- Only 1 disk may be moved each turn.
- A larger disk may never be on top of a smaller disk.

The minimum number of moves required, for *n* disks, is always 2<sup>*n*</sup> - 1.

```python
print([2 ** i - 1 for i in range(1, 10)])
# [1, 3, 7, 15, 31, 63, 127, 255, 511]
```

This puzzle is old and well studied. Notable solutions are binary, recursive, and iterative. 

### Binary

Each disk is represented by a bit. The value of each bit is directly proportional to the size of the disk it represents (i.e. largest bit = largest disk). All bits are off:0 before the first move, stacked on the leftmost rod, and on:1 after the final move.

When successive bits have the same value, the disks they represent are stacked. When successive bits differ, the disk is one position to the left or right of the previous disk.

Decoding the bitstring shows the location of each disk. n = # of larger disks (i.e. more significant bits) stacked on a peg, not including the disk at the base of the stack, +1 if on the initial leftmost peg. If n is even, the disk for the bit of interest is one rod to the right. If n is odd, the disk is one rod to the left. This assumes wrapping, meaning one position left of the leftmost rod equates to the rightmost rod.

The binary solution simply increments by 1 each turn and moves a disk in accord with these rules. Embedded with the bitstring is the position of disks at any point.

For example, take the state of a four disk puzzle after the 5th turn.

```
State after move 5, 0b0101:
0 [4, 1]
1 [2]
2 [3]
```

What is the next move? Disk 1 could be moved from rod 0 to rod 1 or 2, and disk 2 could be moved from rod 1 to rod 2.

Simply increment the binary count by 1, and move the disk to match the above rules.

```
State after move 6, 0b0110:
0 [4, 1]
1 []
2 [3, 2]
```

For 0110, disk 4 must be on a different rod from disk 3, which must be on the same rod as disk 2, which must be a different rod than disk 1.

Furthermore, a bitwise operation can calculate each move via source and destination rods for the *i*th move: 
From rod **( *i* AND *i* - 1) mod 3**, to rod **(( *i* OR *i* - 1 ) + 1) mod 3**.

```
From:                          To:
    0110 (dec 6)                  0110 (dec 6)
AND 0101 (dec 5)               OR 0101 (dec 5)
  = 0100 (dec 4)                = 0111 (dec 7)  
  = 4 % 3                       = ( 7 + 1 ) % 3
  = 1                           = 2
```

The operation indicates to move a disk from rod 1 to rod 2, just as above.




### Python
```python
# binary
def disks(z, a, b):
    z[b].append(z[a].pop())
    for i in range(3):
        print(i, z[i])

def b_toh(n):
    x = [[*range(n, 0, -1)], [], []]
    for i in range(1, 1 << n):
        a = (i & i - 1) % 3
        b = ((i | i - 1) + 1) % 3
        disks(x, a, b)
        print("Move", i, format(i, "#0" + str(n + 2) + "b"))

b_toh(4)
```

### Bash
```bash

```

### PostgreSQL
```sql

```
