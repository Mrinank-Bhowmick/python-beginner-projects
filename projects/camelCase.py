def main():
    var_name = input("camelCase : ")
    print("snakecase :",end=' ')
    for i in var_name:
        if i.isupper():
            print('_'+i.lower(),end='')
        else:
            print(i,end='')
    print(" ")
    
main()
