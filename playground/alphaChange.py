import re
def alphaChange(s):
    alphaRegex = re.compile(r'([a-zA-Z]+)', re.VERBOSE)
    numRegex = re.compile(r'(\d+)', re.VERBOSE)
    groups = alphaRegex.findall(s)
    nums = numRegex.findall(s)
    print(groups)
    strAlpha = ''.join(groups)
    print(strAlpha)
    
    print(nums)
    strNum = ''.join(nums)
    print(strNum)
    
    offset = int(strNum) % 26
    
    print(offset)
    result = ''
    for char in strAlpha:
        print(char)
        code = ord(char)
        print(code)
        base = 90
        if code > 90:
            base = 122
        
        newCode = code + offset
        if newCode > base:
            newCode -= 26
        
        print(newCode)
        newChar = chr(newCode)
        result += newChar
        
    return result
    

print(alphaChange('ab1c'))