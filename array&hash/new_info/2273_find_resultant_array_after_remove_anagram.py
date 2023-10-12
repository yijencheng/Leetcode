# tips: for "same as previous" problem, as we will check previous element, make sure you handle out-of-range cases.

# stack 
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            if len(ans) > 0 and sorted(words[i]) == sorted(ans[-1]):
                continue
            ans.append(words[i])
        return ans


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            if i>0 and sorted(words[i]) == sorted(words[i-1]):
                continue
            ans.append(words[i])
        return ans
                