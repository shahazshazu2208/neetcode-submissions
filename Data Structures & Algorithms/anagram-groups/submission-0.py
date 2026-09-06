class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in res:
                res[key].append(st)
            else:
                res[key] = [st]
        return list(res.values())