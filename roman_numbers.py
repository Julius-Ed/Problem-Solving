def converter(roman_num):

    lookups = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1_000
    }


    edges = {
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "XC" : 90,
        "CD" : 400,
        "CM" : 900
    }

    total = 0

    i = 0
    while i < len(roman_num):

        if roman_num[i:i+2] in edges:
            
            total += edges[roman_num[i:i+2]]
            i+= 2
        else:
            total += lookups[roman_num[i]]
            i += 1
        
    
    return total