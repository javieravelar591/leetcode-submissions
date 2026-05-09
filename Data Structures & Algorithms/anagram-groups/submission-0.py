class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                val = ord(char) - ord('a') # gets distance from start of alphabet
                count[val] += 1
            res[str(count)].append(s)
        return list(res.values())