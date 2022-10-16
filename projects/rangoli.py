N = int(input())

ab = 'abcdefghijklmnopqrstuvwxyz'

def rangoli_line(n,N):
    """ N is rangoli size, n is the number of letters in this line
    """
    center_letter = ab[N-n]
    sides = []
    
    side_length = n-1
    for i in range(side_length):
       sides.append(ab[(N-n)+i+1])
    
    right_side = '-'.join(sides)
    left_side = ''.join(reversed(right_side))
    
    line = left_side + '-' + center_letter + '-' + right_side
    
    return(line)

def rangoli_lines(N):
    if N == 1:
        print('a')
        return
    
    s = []
    for n in range(1,N+1):
        s.append(rangoli_line(n,N))
    
    padding_length = (N - 1)*4 + 1
    for l in s:
        print('{:-^{}}'.format(l, padding_length))
    for l in reversed(s[:-1]):
        print('{:-^{}}'.format(l, padding_length))

rangoli_lines(N)