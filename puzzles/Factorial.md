# Factorial

The *n*! factorial is the product of positive integers less than or equal to n, where 0! = 1. For example, 7! = 7 · 6 · 5 · 4 · 3 · 2 · 1 · 1 = 5040.

> Where 0! = 1,
> 
> *n*! = *n* · (*n* - 1) · (*n* - 2) · (*n* - 3) · ... · 3 · 2 · 1 · 1
>
> Π<sub>*i*=1</sub><sup>*n*</sup>*i* = 1 · 2 · 3 · ... · *n*

Thus the sequence terms are: 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, ...

Write a program to generate the *n*<sup>th</sup> factorial.

### Python
This is a programming exercise, in practice use Python's math.factorial() function.
```python
# recursive, n < 999
def fact(n):
    return 1 if n < 1 else n * fact(n - 1)

def fact(n):
    if n < 1:
        return 1
    return n * fact(n - 1)

# iterative, n < 100000
def fact(n):
    for i in range(1, n):
        n = n * i
    return n

# standard library, n < 200000
from math import prod
def fact(n):
    return prod(range(1, n + 1))
```

### Bash
```bash
# recursive, n < 21
fact() {
  if [ "$1" -lt 1 ]; then
    echo 1
  else
    i=$(fact $(("$1" - 1)))
    echo $(("$1" * i))
  fi
}

# iterative, n < 30000
fact() {
  export BC_LINE_LENGTH=0
  bc <<<"$(seq -s'*' 1 "$1")"
```

### PostgreSQL
As with Python, use PostgreSQL's factorial function in real-world applications.
```sql
-- recursive function, n < 30000
-- echo max_stack_depth = 10GB >> /var/lib/pgsql/13/data/postgresql.conf
-- sed -i '/\[Service\]/aLimitSTACK=infinity' /usr/lib/systemd/system/postgresql-13.service
CREATE OR REPLACE FUNCTION fact (numeric)
    RETURNS numeric
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF $1 = 0 THEN
        RETURN 1;
    ELSE
        RETURN $1 * fact ($1 - 1);
    END IF;
END;
$$;

SELECT
    fact (20);

-- mathematical, n < 400
DO $$
DECLARE
    n integer := 20;
BEGIN
    RAISE NOTICE '%', ROUND(POWER(10, SUM(LOG(CAST(i AS numeric(1000, 990))))))
FROM
    GENERATE_SERIES(1, n) AS i;
END;
$$;

-- variable, n < 30000
DO $$
DECLARE
    n integer := 20;
    i integer := 0;
    j numeric := 1;
BEGIN
    LOOP
        exit
        WHEN i = n;
        i := i + 1;
        SELECT
            j * i INTO j;
    END LOOP;
    RAISE NOTICE '%', j;
END;
$$;

-- tabular iterative, n < 2000
CREATE TABLE fact AS VALUES (1.);

DO $$
DECLARE
    n integer := 20;
BEGIN
    FOR i IN 1..n LOOP
        INSERT INTO fact
        SELECT
            column1 * i
        FROM
            fact
        ORDER BY
            column1 DESC
        LIMIT 1;
    END LOOP;
    RAISE NOTICE '%', *
FROM
    fact
ORDER BY
    column1 DESC
LIMIT 1;
END;
$$;
```

### T-SQL
MSSQL lacks a factorial function, but it still supports recursion.
```sql
-- recursive function, n < 19
IF OBJECT_ID('dbo.fact', 'FN') IS NOT NULL
    DROP FUNCTION dbo.fact;
GO

CREATE FUNCTION dbo.fact (@n numeric)
RETURNS numeric
AS
BEGIN
    IF @n = 0
        RETURN 1;
    RETURN @n * dbo.fact(@n - 1);
END;
GO

SELECT dbo.fact(19);
```
