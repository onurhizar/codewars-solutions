def expand(expr):
    baseStr, exponent = expr.split('^')[0][1:-1], int(expr.split('^')[1])
    if exponent == 0: return '1'
    nonLetters = ['+','-','0','1','2','3','4','5','6','7','8','9']
    def permutation(a,b, output=1):
        for i in range(1,b+1): output *= (a+1-i)/(i)
        return int(output)

    a,b = "","" # (ax+b), parsing
    for letter in baseStr:
        if letter not in nonLetters:
            a,b = baseStr.split(letter)
            b = int(b)
            if a=='': a=1
            elif a=='-': a=-1
            else: a=int(a)

            result = ""
            for exp in range(exponent, -1, -1):
                coef = permutation(exponent, exp) * (a**exp) * (b**(exponent-exp))
                if coef>0: sign='+' 
                else: sign=''
                if coef == 1 and exp!=0: coef=""
                if coef == -1 and exp!=0: coef="-"
                if exp == 1:
                    if  coef == 1: 
                        result += '{}'.format(letter)
                        continue 
                    result += '{}{}{}'.format(sign,coef,letter)
                else: result += '{}{}{}^{}'.format(sign,coef,letter,exp)
            if result[0]=='+': result = result[1:] # remove the beginning plus sign if exists
            return result[:-3]
