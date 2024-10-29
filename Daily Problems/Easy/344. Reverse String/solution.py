# Python solution for 344. Reverse String

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) >> 1): s[i], s[~i] = s[~i], s[i]