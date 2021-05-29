# Tower of Hanoi

This is a puzzle created by Edouard Lucas in 1883. It involves 3 rods with a number of disks of differing size. The puzzle starts with all disks on 1 rod, ordered by size, with the largest disk at the base. It thus resembles a pagoda, where each ascending tier of a tower is smaller than the tier below it. 

![](figures/BaoblazeToH.jpg "10 Ring Tower of Hanoi, courtesy of Baoblaze.")

The goal is to move all disks from 1 rod to another under the following restrictions:

- Only 1 disk may be moved each turn.
- A larger disk may never be on top of a smaller disk.

The minimum number of moves required, for *n* disks, is always 2<sup>*n*</sup> - 1.

```python
print(*[str(i) + ":" + str(2 ** i - 1) for i in range(1, 12)])

# 1:1 2:3 3:7 4:15 5:31 6:63 7:127 8:255 9:511 10:1023 11:2047
```

This puzzle is old and well studied. Notable solutions are binary, recursive, and iterative. 

### Binary

Each disk is represented by a bit. The value of each bit is directly proportional to the size of the disk it represents (i.e. largest bit = largest disk). All bits are off:0 before the first move, stacked on the leftmost rod, and on:1 after the final move.

When successive bits have the same value, the disks they represent are stacked. When successive bits differ, the disk is one position to the left or right of the previous disk.

Decoding the bitstring shows the location of each disk. *n* = # of larger disks (i.e. more significant bits) stacked on a peg, not including the disk at the base of the stack, +1 if on the initial leftmost peg. If *n* is even, the disk for the bit of interest is one rod to the right. If *n* is odd, the disk is one rod to the left. This assumes wrapping, meaning one position left of the leftmost rod equates to the rightmost rod.

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


### Recursive
For a tower of *n* disks, a recursive approach tries to first move *n* - 1, or *m*, disks from one rod to another. Once this is achieved, the final disk can be shifted to the empty rod, and the reverse process again moves the *m* disks on top of it. The same approach is used to solve the initial move of *m* disks; Move *n* - 2 disks from one rod to another.

Take rod 0 as the origin of *n* disks, and rod 2 as the goal. The only state where that largest disk can move from the origin rod 0 to the destination rod 2 is when the other *n* - 1 = *m* disks are on the spare rod 1. Therefore, the 1st goal is moving *m* disks from rod 0 to rod 1.

Similarly, the only state where the largest disk in this reduced set of *m* disks can move to rod 1 is when *m* - 1 disks are on rod 2. To achieve the 1st goal of moving *n* - 1 disks from rod 0 to rod 1, *n* - 2 disks must be moved to rod 2. The target rod thus flips between the spare and end-state target as the number of disks decrements with each recursion; You move three disks from 0 to 2 by moving two disks from 0 to 1, which in turn is done by moving one disk from 0 to 2.


### Iterative
This solution reduces those above into three iterable moves for an even or odd stack. For each move, two rods are given, and one disk shift between them is legal.

- Even: 0-1, 0-2, 1-2.
- Odd: 0-2, 0-1, 1-2.

The resulting solution is optimal in accord with 2<sup>*n*</sup> - 1 turns. This is significant as it determines where in the loop to break to avoid raising exceptions. An even number of disks solves after an odd number of turns, so all three moves are carried out each iteration. An odd number of disks solves after an even number of turns, so all three moves, plus an addition first move from the next iteration, are carried out before breaking.


### Python
```python
# binary
def disk_shift(rods: list, origin: int, target: int) -> None:
    rods[target].append(rods[origin].pop())
    for i in range(3):
        print(i, rods[i])

def b_toh(n: int) -> None:
    b_rods = [[*range(n, 0, -1)], [], []]
    for i in range(1, 1 << n):
        origin = (i & i - 1) % 3
        target = ((i | i - 1) + 1) % 3
        print("Move", i, format(i, "#0" + str(n + 2) + "b"))
        disk_shift(b_rods, origin, target)

b_toh(3)

# recursive, deps: disk_shift()
disks = 3
r_rods = [[*range(disks, 0, -1)], [], []]

def r_toh(n: int, origin: int, target: int, spare: int) -> None:
    if n > 0:
        r_toh(n - 1, origin, spare, target)
        print(n, "from", origin, "to", target)
        disk_shift(r_rods, origin, target)
        r_toh(n - 1, spare, target, origin)

r_toh(disks, 0, 2, 1)

# iterative, deps: disk_shift()
def legal(rods: list, a: int, b: int) -> (int, int):
    if not rods[a]:
        return b, a
    elif not rods[b]:
        return a, b
    elif rods[a][-1] < rods[b][-1]:
        return a, b
    else:
        return b, a

def i_toh(n: int) -> None:
    i_rods = [[*range(n, 0, -1)], [], []]
    while True:
        for i, j in zip([0, 0, 1], [1, 2, 2] if n % 2 == 0 else [2, 1, 2]):
            print(i, j)
            disk_shift(i_rods, *legal(i_rods, i, j))
            if len(i_rods[2]) == n:
                return None

i_toh(4)
```

### Bash
```bash
# binary
w_num() {
  case $1 in
  0) echo "A" ;;
  1) echo "B" ;;
  2) echo "C" ;;
  esac
}

b_toh() {
  A=($(seq "$1" -1 1))
  B=()
  C=()
  for i in $(seq 1 $(((1 << $1) - 1))); do
    declare -n orig=$(w_num $(((i & i - 1) % 3)))
    declare -n targ=$(w_num $((((i | i - 1) + 1) % 3)))
    targ+=("${orig[-1]}")
    unset "orig[-1]"
    echo -e "0: "${A[*]}"\n1: "${B[*]}"\n2: "${C[*]}"\n"
  done
}

b_toh 4

# recursive, 1 disks, 2 origin, 3 target, 4 spare
r_toh() {
  if [ "$1" -gt 0 ]; then
    r_toh $(($1 - 1)) "$2" "$4" "$3"
    echo "$1" from "$2" to "$3"
    r_toh $(($1 - 1)) "$4" "$3" "$2"
  fi
}

r_toh 4 0 2 1

# iterative
legal() {
  a="$1[@]"
  a=("${!a}")
  b="$2[@]"
  b=("${!b}")
  if [ ! "${a[0]}" ]; then
    echo "$2""$1"
  elif [ ! "${b[0]}" ]; then
    echo "$1""$2"
  elif [ "${a[-1]}" -lt "${b[-1]}" ]; then
    echo "$1""$2"
  else
    echo "$2""$1"
  fi
}

i_toh() {
  A=($(seq "$1" -1 1))
  B=()
  C=()
  while true; do
    for i in $([ $((3 % 2)) -eq 0 ] && echo AB AC BC || echo AC AB BC); do
      x=$(legal "${i:0:1}" "${i:1:2}")
      declare -n orig=${x:0:1}
      declare -n targ=${x:1:2}
      targ+=("${orig[-1]}")
      unset "orig[-1]"
      echo -e "0: ${A[*]}\n1: ${B[*]}\n2: ${C[*]}\n"
      if [ "${#B[*]}" -eq "$1" ] || [ "${#C[*]}" -eq "$1" ]; then
        return 0
      fi
    done
  done
}

i_toh 3
```

### PostgreSQL
```sql
-- binary
CREATE OR REPLACE FUNCTION b_toh (int)
    RETURNS varchar
    LANGUAGE 'plpgsql'
    AS $$
DECLARE
    orig numeric;
    targ numeric;
BEGIN
    FOR i IN 1.. (1 << $1) - 1 LOOP
        orig := (i & i - 1) % 3;
        targ := ((i | i - 1) + 1) % 3;
        RAISE NOTICE 'Move %: From % to %', i, orig, targ;
    END LOOP;
END;
$$;

SELECT
    b_toh (3);

-- recursive
CREATE OR REPLACE FUNCTION r_toh (int, int, int, int)
    RETURNS varchar
    LANGUAGE 'plpgsql'
    AS $$
BEGIN
    IF $1 > 0 THEN
        RETURN r_toh ($1 - 1, $2, $4, $3) || $1 || ' from ' || $2 || ' to ' || $3 || E'\n' || r_toh ($1 - 1, $4, $3, $2);
    ELSE
        RETURN '';
    END IF;
END;
$$;

SELECT
    r_toh (3, 0, 2, 1);
```
