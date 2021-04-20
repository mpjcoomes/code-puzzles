# Symbol Tree
Write a program that outputs a symmetrical symbol tree for *n* rows. For example, if asterisk is the symbol and *n* = 5, then stdout:

         *
        ***
       *****
      *******
     *********

Optionally, decorate the tree.

### Python
```python
# iterative
def shrub(n):
    for i, j in zip(range(n, 0, -1), range(1, n * 2, 2)):
        print(" " * i, "*" * j)

# iterative string print
def shrub(n):
    print(
        *[" " * i + "*" * j for i, j in zip(range(n)[::-1], range(1, n * 2, 2))],
        sep="\n"
    )

# decorated
def xmas_tree(n):
    j = 1
    k = n
    print(*[" " * n + "@"])
    for i in range(n)[::-1]:
        print(" " * i, "*" * j)
        j += 2
    print(*[" " * k + "|"])
```

### Bash
```bash
# C syntax loop
shrub() {
  for ((i = $1, j = 1; i > 0; i--, j+++2)); do
    printf ' %.0s' $(seq 1 $i)
    printf '*%.0s' $(seq 1 $j)
    echo ''
  done
}

# bash iterative
n=8
j=1
for i in $(seq 1 "$n" | sort -rn); do
  printf ' %.0s' $(seq 1 $i)
  printf '*%.0s' $(seq 1 $j)
  echo ''
  j=$(( j + 2 ))
done
```

### PostgreSQL
```sql
-- functional
CREATE OR REPLACE FUNCTION tree (n INT)
	RETURNS TABLE (k TEXT)
LANGUAGE 'plpgsql'
AS $$
BEGIN
	RETURN QUERY
		WITH tree AS (
			SELECT j, row_number() over () AS i
			FROM generate_series(2*n-1, 0, -2) AS j
		)
		SELECT repeat(' ', i::INT) || repeat('*', j) AS k
		FROM tree
		ORDER BY k;
END; $$;

SELECT tree(10);

-- iterative, tabular
CREATE TABLE tree (dummy VARCHAR);
do $$
declare
	n integer := 5;
	j integer := 1;
begin
	loop
		exit when n = 0;
			INSERT INTO tree
			select REPEAT(' ', n) || REPEAT('*', j);
			n := n - 1;
			j := j + 2;
	end loop;
end; $$;

SELECT *
FROM tree;

-- query, n = 10
WITH tree AS (
	SELECT generate_series(10, 1, -1) AS i,
	generate_series(1, 2*10-1, 2) AS j
)
SELECT repeat(' ', i) || repeat('*', j) AS k
FROM tree;
```
