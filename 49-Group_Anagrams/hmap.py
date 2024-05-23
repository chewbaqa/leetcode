# map each charactercount to list of anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for each in strs:
            count = [0] * 26
            for charac in each:
                count[ord(charac) - ord("a")] += 1
            hmap[tuple(count)].append(each)
        return hmap.values()
