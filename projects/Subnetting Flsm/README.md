# Subnetting_FLSM

Subnetting_FLSM is developed for:
1.Calculation and analyzing number of hosts
2.Distribution hosts for each subnet by FLSM method
3.Transferring unique network address, broadcast address, usable hosts

## Example

```text
Network address: 192.168.1.0
Prefix of network: 24
Num of subnets: 4
Max value of hosts for one sub: 30

                         Subnetting - FLSM
Network address/prefix     Number of subnets     Max num of hosts for one sub
    192.168.1.0/24                 4                         30

№Net     Value of hosts          Network address     Broadcast address          Usable hosts
1              30                  192.168.1.0          192.168.1.31        192.168.1.1 - 192.168.1.30
2              30                  192.168.1.32         192.168.1.63        192.168.1.33 - 192.168.1.62
3              30                  192.168.1.64         192.168.1.95        192.168.1.65 - 192.168.1.94
4              30                  192.168.1.96         192.168.1.127       192.168.1.97 - 192.168.1.126
```

## How to run on localhost

```
python subnetting_flsm.py
```

## Dependencies

Standard library only.
