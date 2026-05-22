# Health Management System

A console-based health log. It lets you log exercise or food entries (timestamped) for one of three users into text files, and retrieve those logs later.

## Example

```text
health management system:
Press 1 for log the value and 2 for retrieve 1
Press 1 for anu 2 for simon 3 for john 1
Enter 1 for excerise and 2 for food :1
type here..
30 min morning run
written successfully
```

Retrieving a log:

```text
health management system:
Press 1 for log the value and 2 for retrieve 2
Press 1 for anu 2 for simon 3 for john 1
enter 1 for exercise and 2 for food1
['2024-03-15 08:12:34.123456']: 30 min morning run
```

## How to run on localhost

```
python health.py
```

## Dependencies

Standard library only (`datetime`).
