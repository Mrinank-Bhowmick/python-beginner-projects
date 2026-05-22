# IPv4_Calculator

IPv4_Calculator is developed for:
1.Determine the network class (A, B, C);
2.Determine which category the address belongs to (private, public);
3.Determine subnet attributes.

## Example

```text
Enter IP address of host: 192.168.1.10
Enter IP prefix: 24
IP address: 192.168.1.10/24
Class of IP address: C
Address category: Private
Host address (decimal): [192, 168, 1, 10]
Mask (decimal): [255, 255, 255, 0]
Network address (decimal): [192, 168, 1, 0]
Broadcast address (decimal): [192, 168, 1, 255]
First available host (decimal): [192, 168, 1, 1]
Last available host (decimal): [192, 168, 1, 254]
Host address(binary): ['11000000', '10101000', '00000001', '00001010']
Mask(binary): ['11111111', '11111111', '11111111', '00000000']
Network address(binary): ['11000000', '10101000', '00000001', '00000000']
Broadcast address(binary): ['11000000', '10101000', '00000001', '11111111']
First available host (binary): ['11000000', '10101000', '00000001', '00000001']
Last available host (binary): ['11000000', '10101000', '00000001', '11111110']
Total Number of Hosts: 256
Number of Usable Hosts: 254
```

## How to run on localhost

```
python ipv4_calc.py
```

## Dependencies

Standard library only.
