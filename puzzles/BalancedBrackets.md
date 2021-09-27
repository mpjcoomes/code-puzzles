# Balanced Brackets

Test a string of brackets to determine whether every opening bracket has a matching closing bracket of the same type.

```
[][]  	            OK
({[})]	            OK
[[){}(]]            FAIL
[[[[]]]             FAIL
[[[{][[]][]](}())]  OK
```

### Python
```python
# recursive
def flib(x: str) -> str:
    return "]" if x == "[" else ")" if x == "(" else "}"

def bb(x: str) -> str:
    if x[0] == "]" or x[0] == ")" or x[0] == "}" or len(x) % 2 == 1:
        return "Desequilibre"
    elif x == "[]" or x == "()" or x == "{}":
        return "Egal"
    else:
        x = x.replace(x[0], "", 1).replace(flib(x[0]), "", 1)
        return bb(x)

bb("([{])}")
```

### Bash
```bash
# recursive
flib() {
  case "${1}" in
  "[") echo "]" ;;
  "{") echo "}" ;;
  "(") echo ")" ;;
  esac
}

bb() {
  z=$(cut -c1 <<<$1)
  if [[ "$z" == "]" || "$z" == ")" || "$z" == "}" || $((${#1} % 2)) == 1 ]]; then
    echo "FAIL"
    return 0
  elif [[ "$1" == "[]" || "$1" == "()" || "$1" == "{}" ]]; then
    echo "PASS"
    return 0
  else
    x=${1#$z}
    x=${x/$(flib "$z")}
    bb "$x"
  fi
}

bb "(){[][()}]"
```

### PostgreSQL
```sql
```
