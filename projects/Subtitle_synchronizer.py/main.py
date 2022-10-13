def convertToMilliseconds(time):
    # convert the timestamp into milliseconds
    milliseconds = 0
    hh, mm, ms = time.split(":")
    ms = ms.strip().replace(",", "")
    hh = int(hh)
    mm = int(mm)
    ms = int(ms)

    milliseconds = hh * 3600000 + mm * 60000 + ms
    return milliseconds


def synchronize(time, shift):
    # calculate new time by applying the shift
    return time - shift


def convertToTime(milliseconds):
    # convert milliseconds into timestamp
    hh = milliseconds // 3600000
    milliseconds = milliseconds % 3600000
    hh = str(hh)
    if len(hh) < 2:
        hh = "0" + hh

    mm = milliseconds // 60000
    milliseconds = milliseconds % 60000
    mm = str(mm)
    if len(mm) < 2:
        mm = "0" + mm

    ss = milliseconds // 1000
    milliseconds = milliseconds % 1000
    ss = str(ss)
    if len(ss) < 2:
        ss = "0" + ss

    milliseconds = str(milliseconds)
    while len(milliseconds) < 3:
        milliseconds = "0" + milliseconds

    return f"{hh}:{mm}:{ss},{milliseconds}"


def main():
    SHIFT = int(input("Please enter the shift in milliseconds: "))

    # opening the file input.srt
    f = open("input.srt", "r", errors="ignore")
    output = open("output.srt", "a")
    for x in f:
        if "-->" in x:
            # applying the changes and re-writing into the output file
            start, end = x.split("-->")
            start, end = convertToMilliseconds(start), convertToMilliseconds(end)
            start, end = synchronize(start, SHIFT), synchronize(end, SHIFT)
            start, end = convertToTime(start), convertToTime(end)
            output.write(f"{start} --> {end}\n")
        else:
            # no changes if the line is not a timestamp
            output.write(x)


main()
