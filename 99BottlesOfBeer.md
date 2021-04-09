# 99 Bottles of Beer

Print lyrics for "99 Bottles of Beer on the Wall" from 99 to 0, grammatically correct.
```
99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall

...

1 bottle of beer on the wall
1 bottle of beer
Take one down, pass it around
0 bottles of beer on the wall
```

### python
```python

```

### bash
```bash
a="bottles of beer"
b="on the wall"
c="Take one down, pass it around"

for i in {99..1}; do
  if (( i > 2 )); then
    echo -e "$i $a $b\n$i $a\n$c\n$(( i -1 )) $a $b\n"
  elif (( i == 2 )); then
    echo -e "$i $a $b\n$i $a\n$c"
    echo -e "$(( i -1 )) $a $b\n" | tr -d s
  else
    echo -e "$i $a $b\n$i $a" | tr -d s
    echo -e "$c\n$(( i -1 )) $a $b"
  fi
done
```

### PostgreSQL
```sql
SELECT CASE
	WHEN j = 0 AND i = 1 THEN i || ' ' || 'bottle of beer on the wall'
	WHEN j = 0 THEN i || ' ' || 'bottles of beer on the wall'
	WHEN j = 1 AND i = 1 THEN i || ' ' || 'bottle of beer'
	WHEN j = 1 THEN i || ' ' || 'bottles of beer'
	WHEN j = 3 AND i = 2 THEN  i - 1  || ' ' || 'bottle of beer on the wall'
	WHEN j = 3 THEN i - 1  || ' ' || 'bottles of beer on the wall'
	WHEN j = 2 THEN 'Take one down, pass it around'
	ELSE ''
	END AS A
FROM GENERATE_SERIES(1,99) AS i,
	GENERATE_SERIES(0,4) AS j
ORDER BY i DESC, j;
```
