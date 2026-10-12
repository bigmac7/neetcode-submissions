class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "~" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        prev = 0
        for i, char in enumerate(s):
            if char == "~":
                length = int(s[prev:i]) #everything before delimiter
                res.append(s[i+1:i+1+length])
                prev = i + length + 1
        return res




