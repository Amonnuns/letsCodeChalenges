

from posixpath import split


def romanToInt(s):
    mySymbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    romanNumbers = list(s)

    sum = 0
    i= 0
    while i < len(romanNumbers):
        if(i == (len(romanNumbers)-1)):
            if (mySymbols[romanNumbers[i]] <= mySymbols[romanNumbers[i-1]]):
                sum+=mySymbols[romanNumbers[i]]
            break
        elif(mySymbols[romanNumbers[i]] >= mySymbols[romanNumbers[i+1]]):
            sum+=mySymbols[romanNumbers[i]]
            i+=1
        elif(mySymbols[romanNumbers[i]] < mySymbols[romanNumbers[i+1]]):
            sum+=(mySymbols[romanNumbers[i+1]]-mySymbols[romanNumbers[i]])
            i+=2
    
    return sum

print(romanToInt("DCXXI"))