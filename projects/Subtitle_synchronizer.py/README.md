# Subtitle Synchronizer

A console tool that shifts all timestamps in an SRT subtitle file by a given number of milliseconds, reading from `input.srt` and writing the synchronized result to `output.srt`.

## Example

```text
Please enter the shift in milliseconds: 2000
```

Given an `input.srt` containing timestamps like:

```text
1
00:00:05,000 --> 00:00:08,500
Hello, world!
```

The resulting `output.srt` shifts every timestamp back by 2000 ms:

```text
1
00:00:03,000 --> 00:00:06,500
Hello, world!
```

## How to run on localhost

```
python main.py
```

Place an `input.srt` file in the same folder before running.

## Dependencies

Standard library only.
