class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        try:
            for schar, tchar in zip(s,t, strict=True):
                s_map[schar] += 1
                t_map[tchar] += 1
        except ValueError:
            return False
        return s_map == t_map
        