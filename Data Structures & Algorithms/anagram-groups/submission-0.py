from collections import Counter, defaultdict
from itertools import groupby
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group by length first.
        #create counter for each str
        #add first to it's own List
        #compare counter with first, if not, add to own List
        #next one compare with first counter, if not add to own List
        # ...
        groups = defaultdict(list)
        for string in strs:
            key = frozenset(Counter(string).items())
            groups[key].append(string)

        return list(groups.values())

        