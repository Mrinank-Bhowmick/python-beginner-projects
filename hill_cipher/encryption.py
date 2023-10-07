import mysql.connector as c;

con = c.connect(host = "", user = "", password = "")
cur = con.cursor()
cur.execute("use hillcipher")


#to perform the modulus operation
def mod(num):
    if num<0:
        result = 26 - (abs(num)%26)

    else:
        result = num%26
    return result



#the algorithm of hill cipher using the key

def hill_cipher(text,key_matrix):
    cipher_text = []
    sum = 0
    for i in range(3):
        sum+=(text[i]-1)*key_matrix[i]
    cipher_text.append(sum)


    sum = 0
    for i in range(3,6):
        sum+=(text[i-3]-1) * key_matrix[i]
    cipher_text.append(sum)

    sum=0
    for i in range(6,9):
        sum+=(text[i-6]-1) * key_matrix[i]
    cipher_text.append(sum)
    return cipher_text



#to hill cipher the password and return the hill ciphered text
#main function to be imported
def message(actual_text):
    HillCipherText=" "
    sect =[]
    matrix=[]

    for i in range(3):
        sect.append(actual_text[i])
    for i in range(3):
        cur.execute(f"select lid from loalpha where lchar = '{sect[i]}'")
        l = cur.fetchone()
        for i in l:
           matrix.append(i)

    l = [17, 21, 2, 17, 18, 2, 5, 21, 19]
    h =hill_cipher(matrix,l)

    for i in h:
        r = mod(i)
        cur.execute(f"select lchar from loalpha where lid = {r+1}")
        t = cur.fetchone()

        HillCipherText+=t[0]

    return HillCipherText

if __name__=="__main__":
    Message=input("enter your message")
    p = message(Message)
    print(p)

