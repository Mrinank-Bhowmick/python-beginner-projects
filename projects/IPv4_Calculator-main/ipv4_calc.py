def pr(name, mask):
    return name + mask


def ip_correct_check(octet):
    check = octet.split(".")
    counter = 0
    for i in check:
        if 0 <= int(i) <= 255:
            counter += 1
        else:
            return False
        if counter == 4:
            return True


# IP address of host
ip_addr = input("Enter IP address of host: ")

while True:
    if ip_correct_check(ip_addr):
        break
    else:
        ip_addr = input("Enter correct IP address of host: ")

# Mask --- prefix
ip_prefix = int(input("Enter IP prefix: "))

while True:
    if 0 <= ip_prefix <= 31:
        break
    else:
        ip_prefix = input("Prefix can be in range [0, 31]: ")


# IP class
ip_list_octet = ip_addr.split(".")
ip_list_octet = [int(i) for i in ip_list_octet]
class_of_ip = None  # IP class ----------


if int(ip_list_octet[0]) in range(0, 128):
    class_of_ip = "A"
elif int(ip_list_octet[0]) in range(128, 191):
    class_of_ip = "B"
elif int(ip_list_octet[0]) in range(191, 224):
    class_of_ip = "C"
elif int(ip_list_octet[0]) in range(224, 240):
    class_of_ip = "D"
elif int(ip_list_octet[0]) in range(240, 255):
    class_of_ip = "E"


# Public/private
type_of_ip = None
if (
    (int(ip_list_octet[0]) == 10)
    or (int(ip_list_octet[0]) == 172 and int(ip_list_octet[1]) in range(16, 32))
    or (int(ip_list_octet[0]) == 192 and int(ip_list_octet[1]) == 168)
):
    type_of_ip = "Private"
else:
    type_of_ip = "Public"


# Mask bin/dec
mask_bin = int(ip_prefix) * "1" + (32 - int(ip_prefix)) * "0"

mask_bin_list = []
for i in range(0, len(mask_bin), 8):
    mask_bin_list.append(mask_bin[i : i + 8])


mask_dec_list = [int(("0b" + i), 2) for i in mask_bin_list]


# IP Addr bin
def ip_in_bin(octet):
    m = str(bin(octet))
    m1 = [i for i in m]
    m1 = m1[2::]
    if len(m1) != 8:
        for i in range(0, 8 - len(m1)):
            m1.insert(0, "0")
    m2 = ["".join(m1)]
    return m2


bin_ip_list = []  # IP Addr bin----------------
for i in range(len(ip_list_octet)):
    bin_ip_list.insert(i, ip_in_bin(int(ip_list_octet[i])))
    bin_ip_list[i] = bin_ip_list[i][0]


# Subnet add dec
subnet_decimal_list = []
for i in range(4):
    subnet_decimal_list.append(
        int(("0b" + mask_bin_list[i]), 2) & int(("0b" + bin_ip_list[i]), 2)
    )


# Subnet add bin
subnet_bin_list = []
for i in range(len(ip_list_octet)):
    subnet_bin_list.insert(i, ip_in_bin(int(subnet_decimal_list[i])))
    subnet_bin_list[i] = subnet_bin_list[i][0]

# Broadcast dec
broadcast_dec = []
for i in range(4):
    if mask_dec_list[i] == 255:
        broadcast_dec.append(int(ip_list_octet[i]))
    elif mask_dec_list[i] == 0:
        broadcast_dec.append(255)
    else:
        prom_broadcast_num = 256 - mask_dec_list[i]
        prom_broadcast_final = 0
        while prom_broadcast_final < int(ip_list_octet[i]):
            prom_broadcast_final += prom_broadcast_num
        prom_broadcast_final -= 1
        broadcast_dec.append(prom_broadcast_final)

# Broadcast bin
broadcast_bin = []
for i in range(4):
    broadcast_bin.insert(i, ip_in_bin(int(broadcast_dec[i])))
    broadcast_bin[i] = broadcast_bin[i][0]

# First/Last available host dec
if 1 <= int(ip_prefix) <= 30:
    first_av_host = subnet_decimal_list[:3] + [subnet_decimal_list[3] + 1]
else:
    first_av_host = subnet_decimal_list[:3] + [subnet_decimal_list[3]]


last_av_host = []
if 1 <= int(ip_prefix) <= 8:
    last_av_host = [subnet_decimal_list[0] + 2 ** (8 - int(ip_prefix)) - 1] + [
        255,
        255,
        254,
    ]
elif 9 <= int(ip_prefix) <= 16:
    last_av_host = (
        subnet_decimal_list[:1]
        + [subnet_decimal_list[1] + 2 ** (16 - int(ip_prefix)) - 1]
        + [255, 254]
    )
elif 17 <= int(ip_prefix) <= 24:
    last_av_host = (
        subnet_decimal_list[:2]
        + [subnet_decimal_list[2] + 2 ** (24 - int(ip_prefix)) - 1]
        + [254]
    )
elif 25 <= int(ip_prefix) <= 30:
    last_av_host = subnet_decimal_list[:3] + [
        subnet_decimal_list[3] + 2 ** (32 - int(ip_prefix)) - 2
    ]
elif int(ip_prefix) == 31:
    last_av_host = subnet_decimal_list[:3] + [
        subnet_decimal_list[3] + 2 ** (32 - int(ip_prefix)) - 1
    ]

# First/Last available host bin
first_bin_list = []
for i in range(len(ip_list_octet)):
    first_bin_list.insert(i, ip_in_bin(int(first_av_host[i])))
    first_bin_list[i] = first_bin_list[i][0]

last_bin_list = []
for i in range(len(ip_list_octet)):
    last_bin_list.insert(i, ip_in_bin(int(last_av_host[i])))
    last_bin_list[i] = last_bin_list[i][0]

# Available number of addresses
available_number_prom = 32 - ip_prefix
available_number = 2**available_number_prom


# Output---------------------------------------------------------
# -------------------------------------------------------------
print("IP address: {}/{}".format(ip_addr, ip_prefix))
print("Class of IP address: {}".format(class_of_ip))
print("Address category: {}".format(type_of_ip))
print("Host address (decimal): {}".format(ip_list_octet))
print("Mask (decimal): {}".format(mask_dec_list))
print("Network address (decimal): {}".format(subnet_decimal_list))
print("Broadcast address (decimal): {}".format(broadcast_dec))
print("First available host (decimal): {}".format(first_av_host))
print("Last available host (decimal): {}".format(last_av_host))

print("Host address(binary): {}".format(bin_ip_list))
print("Mask(binary): {}".format(mask_bin_list))
print("Network address(binary): {}".format(subnet_bin_list))
print("Broadcast address(binary): {}".format(broadcast_bin))
print("First available host (binary): {}".format(first_bin_list))
print("Last available host (binary): {}".format(last_bin_list))
print("Total Number of Hosts: {}".format(available_number))
print("Number of Usable Hosts: {}".format(available_number - 2))
