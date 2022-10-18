import socket
import pyfiglet


port_to_check = 22


def port_checker(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("127.0.0.1", port))
    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")

    sock.close()


print(pyfiglet.figlet_format("Port Scanner"))
print("Is port {} open?".format(port_to_check))
port_checker(port_to_check)
