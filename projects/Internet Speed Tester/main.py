# pip install pyspeedtest
# pip install speedtest
# pip install speedtest-cli

import speedtest

speedTest = speedtest.Speedtest()
print(speedTest.get_best_server())
# Check download speed
print(speedTest.download())
# Check upload speed
print(speedTest.upload())
