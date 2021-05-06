# 99 Bottles of Beer
Print lyrics for "99 Bottles of Beer on the Wall" from 99 to 0, grammatically correct.

	99 bottles of beer on the wall
	99 bottles of beer
	Take one down, pass it around
	98 bottles of beer on the wall

	...

	1 bottle of beer on the wall
	1 bottle of beer
	Take one down, pass it around
	0 bottles of beer on the wall

### Python
```python
a = "bottles of beer"
b = "on the wall"
c = "Take one down, pass it around"

for i in range(99, 0, -1):
    if i > 2:
        print(i, a, b, "\n" + str(i), a, "\n" + c, "\n" + str(i - 1), a, b, "\n")
    elif i == 2:
        print( i, a, b, "\n" + str(i), a, "\n" + c, "\n" + str(i - 1), a.replace("s", ""), b, "\n", )
    else:
        print( i, a.replace("s", ""), b, "\n" + str(i), a.replace("s", ""), "\n" + c, "\n" + str(i - 1), a, b, "\n", )
```

### Bash
```bash

a="bottles of beer on the wall"
b="Take one down, pass it around"

for i in {99..1}; do
  if (( i > 2 )); then
    echo -e "$i $a\n$i ${a% on*}\n$b\n$(( i -1 )) $a\n"
  elif (( i == 2 )); then
    echo -e "$i $a\n$i ${a% on*}\n$b"
    echo -e "$(( i -1 )) $a\n" | tr -d s
  else
    echo -e "$i $a\n$i ${a% on*}" | tr -d s
    echo -e "$b\n$(( i -1 )) $a"
  fi
done
```

### PostgreSQL
```sql
WITH bottles AS (
SELECT i, j, CASE
	WHEN j = 0 THEN i || ' bottles of beer on the wall'
	WHEN j = 1 THEN i || ' bottles of beer'
	WHEN j = 2 THEN 'Take one down, pass it around'
	WHEN j = 3 THEN i - 1 || ' bottles of beer on the wall'
	ELSE ''
	END AS A
FROM GENERATE_SERIES(1,99) AS i,
	GENERATE_SERIES(0,4) AS j
)
SELECT CASE
	WHEN CAST(substring(A, '^1\s') AS INTEGER) = 1 THEN translate(A, 's', '')
	ELSE A
	END
FROM bottles
ORDER BY i DESC, j;
```
