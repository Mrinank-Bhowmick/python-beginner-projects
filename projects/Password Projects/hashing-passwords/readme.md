# hashing passwords
## Execute
> python hashing_passwords.py <password> [-t {sha256,sha512,md5}] ` 

*※ Default hash-type is sha256*

## Example
```
$ python hashing_passwords.py Github
< hash-type : sha256 >
1720d8eaff790da6af4406905ba663d0cc6a6cea2b3e54e7384ac334a037f59d
```
```
$ python hashing_passwords.py Github
< hash-type : sha512 >
567efaa953d9c7f53865ab6efca82ddd1031d772503352c5ac992f0ca7eef88ddf523ba7e1d049b0d3559941679697be2b874bfb68e5fc0dc8eb37aa204fcca9
```