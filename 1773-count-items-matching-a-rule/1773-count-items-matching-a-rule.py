class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            i = 0
        if ruleKey == "color":
            i = 1
        if ruleKey == "name":
            i = 2
        n = len(items)
        for j in range(n):
            if items[j][i] == ruleValue:
                count += 1
        return count
        