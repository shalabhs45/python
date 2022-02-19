
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        p = re.compile('[-+]?[0-9]+')
        str = str.strip()
        m = p.match(str)
        rev = int(m.group()) if m else ''
                
        if not rev:
            return 0
        
        elif rev < -2147483648:
            return -2147483648
        elif rev > 2147483647:
            return 2147483647
        else:
            return rev