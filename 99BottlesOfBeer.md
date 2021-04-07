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

```
