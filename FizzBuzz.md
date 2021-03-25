# FizzBuzz
Print the integers from 1 to 100 inclusive. For multiples of three, print Fizz instead of the number. For multiples of five, print Buzz instead of the number. For multiples of both three and five, print FizzBuzz instead of the number.

### python
``` python
for i in range(1, 101):
	if i % 15 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)
```

### bash
``` bash
for i in {1..100}; do
	((( i % 15 == 0 )) && echo 'FizzBuzz') ||
	((( i % 5 == 0 )) && echo 'Buzz') ||
	((( i % 3 == 0 )) && echo 'Fizz') ||
	echo $n;
done
```

### SQL
``` sql
SELECT CASE
	WHEN MOD(level,15)=0 THEN 'FizzBuzz'
	WHEN MOD(level,3)=0 THEN 'Fizz'
	WHEN MOD(level,5)=0 THEN 'Buzz'
	ELSE TO_CHAR(level)
	END FizzBuzz
FROM dual
CONNECT BY LEVEL <= 100;
```
