# This CLI script checks if entered ips are or
# aren`t blacklisted on different lists
# You need to register and get API key on blacklistchecker.com
# to make it work (it`s free 30 or 50 IPs per month)

import json
import re
import sys
from typing import Any

import requests

api_key = "key_CAMF5HI5t4ZzkmgGkioI1tius"  # API key for requests to work. Free 50 IP checks per month on blacklistchecker.com


def test_ip(ip: str) -> Any:
    link = f"https://api.blacklistchecker.com/check/{ip}"
    result = requests.get(
        link, auth=(api_key, "")
    )  # writing response from service into a var
    result_dec = json.loads(result.content)  # decoding json result
    print(result_dec)
    detects: list[str] = []
    if result_dec.get("statusCode") == 401:
        res = "limit exceeded!"
        return (res, detects)
    elif result_dec.get("detections") != 0:
        res = ip
        blsts = result_dec.get("blacklists")
        for n in blsts:
            if n.get("detected") is True:
                detects.append(n.get("name"))
        return (
            res,
            detects,
        )  # function returns IP and list of blacklists (haha), if any are detected.


def isip(ip: str) -> bool:
    match = re.match(
        r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip
    )  # this regex is checking if provided string contains 4 numeric blocks 1 to 3 symbols divided by a dot.
    if not bool(match):
        return False
    return all(
        0 <= int(octet) <= 255 for octet in ip.split(".")
    )  # this line checks if blocks from regex are numbers between 0 and 255


res_txt = "IP blacklists check returned next results:\n"
send_param = 0
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        if isip(x) is not True:
            print(f"IP {x} is incorrect\n")
        else:
            if test_ip(x) is not None:
                res, detec = test_ip(x)
                if res == "limit exceeded":
                    res_txt = res_txt + " LIMIT Exceeded!"
                    break
                else:
                    res_txt += f"{res} is detected in {detec} blacklists \n \n"
else:
    print("Type in ip to check")
    x = input()
    if isip(x) is not True:
        print(f"IP {x} is incorrect\n")
    else:
        if test_ip(x) is not None:
            res, detec = test_ip(x)
            if res == "limit exceeded":
                res_txt = res_txt + "Limit Exceeded!\n"
            else:
                res_txt += f"{res} is detected in {detec} blacklists \n \n"
if len(res_txt) <= 43:
    print("IPs not blacklisted!")
    print(res_txt)
else:
    print("Blacklist check result is: \n" + res_txt)
