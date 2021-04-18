# Symbol Tree
Write a program that outputs a symmetrical symbol tree for *n* rows. For example, if asterisk is the symbol and *n* = 5, then stdout:

         *
        ***
       *****
      *******
     *********


### Python
```python
def shrub(n):
    for i, j in zip(range(n, 0, -1), range(1, n * 2, 2)):
        print(" " * i, "*" * j)
```

### Bash
```bash
shrub() {
  for ((i = $1, j = 1; i > 0; i--, j++, j++)); do
    printf ' %.0s' $(seq 1 $i)
    printf '*%.0s' $(seq 1 $j)
  done
}
```

### PostgreSQL
```sql

```
