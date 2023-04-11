'''MY 1ST OWN METHOD 
    THIS METHOD ISN'T PRESENT ANYWHERE ON THE NET
    ALL PERMUTATIONS OF 0 & 1 FOR 'n' DIGITS
    WITHOUT ANY LIBRARY SUPPORT,PREDEFINED MATHEMATICAL FUNCTIONS
    AND IT'S GENERALIZED FOR ALL 'n' NO OF DIGITS
    I KNOW THIS METHOD ISN'T PERFECT BUT AS A BEGINNER I HAVE JUST TRIED
    TO MAKE SOMETHING AT MY OWN.
    ###        RACHIT        JOSHI        ###'''

#defining a function for permutation 
def _rj_(n):
    a=int((bin(2**(n-1))),2)
    b=int((bin((2**n)-1)),2)
    l=[]
    for i in range(a,b+1):
        i=str(bin(i))
        l.append(i[2:1+len(i)])
    b=''
    l1=[]
    for i in l:
        for j in i:
            if j=='0':
                b+='1'
            elif j=='1':
                b+='0'
        l1.append(b)
        b=''
    l=l+l1
    l.sort()
    #printing output
    print('Your Combo\'s:',l)
    print('No. of Combo\'s:',len(l))

#taking input for no. of digits as n
n=int(input("enter no. of digits"))
_rj_(n)    