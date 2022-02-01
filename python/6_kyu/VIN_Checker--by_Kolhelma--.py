#2021-07-30 12:13:41.189000+00:00
"""# VIN Checker

In this Kata you should write a function to validate VINs, Vehicle Identification Numbers. Valid VINs are exactly 17 characters long, its composed of capital letters (except "I","O" and "Q") and digits. The 9th character is a MODULUS 11 check digit. Here is how it works:

## 1. Letters are converted to numbers

Following the table bellow, letters are converted to numbers. "I","O" and "Q" are invalid characters.

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    1 2 3 4 5 6 7 8   1 2 3 4 5   7   9 2 3 4 5 6 7 8 9

 Ex.: VIN **5YJ3E1EA7HF000337** becomes **58135151786000337**.

## 2. Each number is multiplied by a weight

The weights are the following: **[8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]**.

    Ex.:
    VIN:     5   Y   J   3   E   1   E   A   7   H   F   0   0   0   3   3   7
    DECODED: 5   8   1   3   5   1   5   1   7   8   6   0   0   0   3   3   7
    WEIGHTS: 8   7   6   5   4   3   2   10  0   9   8   7   6   5   4   3   2
    PRODUCT: 40  56  6   15  20  3   10  10  0   72  48  0   0   0   12  9   14

## 3. All products are summed up

    Ex.:
    40+56+6+15+20+3+10+10+0+72+48+0+0+0+12+9+14 = 315

## 4. The modulus 11 of the sum is taken

    Ex.:
    315 mod 11 = 7

## 5. Check 9th character

If the 9th character matches the modulus 11, the VIN is valid.

    Ex.:
    5YJ3E1EA7HF000337 is a valid VIN, 9th character is 7

### Note

If the modulus 11 of the sum is equal to 10, then the digit is "X".

    Ex.: 
    5YJ3E1EAXHF000347 is a valid VIN.

### Input Validation

Input validation is part of the Kata, VINs with lenghts different than 17 characters or containing invalid characters should return `False` as well.

### Online VIN Checker

[Click here](https://vpic.nhtsa.dot.gov/decoder/CheckDigit/Index/5YJ3E1EA7HF000337) to open an online VIN Checker if you want to better understand how it works."""


values = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'J':1,'K':2,'L':3,'M':4,'N':5,'P':7,'R':9,'S':2,'T':3,'U':4,'V':5,'W':6,'X':7,'Y':8,'Z':9}
weights = {'0':8, '1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':10,'8':0,'9':9,'10':8,'11':7,'12':6,'13':5,'14':4,'15':3,'16':2}
import re
not_good_chars = set('OQI')
letters = re.compile('[A-Z]')
def check_vin(number):
    nr = []
    number = number.upper()
    if any((c in not_good_chars) for c in number) or len(number) != 17:
        return False
    numberA = re.sub(letters, lambda x: str(values[x.group()]), number)
    for i,v in enumerate(numberA):
        new_num = int(v) * int(weights[str(i)])
        nr.append(new_num)
    sum_nr_mod = sum(nr) % 11
    print ('sum nr: ' + str(sum(nr)))
    print ('nr mod yra: ' + str(sum_nr_mod))
    print ('astuntas nr/raide yra: ' + str(number[8]))
    print ('konvertuotas astuntas NR yra: ' + str(numberA[8]))
    print (number)
    if sum_nr_mod == 10:
        if  number[8] == 'X':
            return True
        else:
            return False
    if number[8] == 'X' and sum_nr_mod !=0:
        return False
    if int(sum_nr_mod) ==int(numberA[8]):
        return True
    else:
        print('a')
        return False