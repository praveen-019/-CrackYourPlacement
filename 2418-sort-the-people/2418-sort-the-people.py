class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict = {}
        n = len(names)
        for i in range(n):
            dict[heights[i]] = names[i]
        dict = sorted(dict.items(),key=lambda item:item[0])
        names.clear()
        for i in dict:
            names.append(i[1])
        return names[::-1]
        