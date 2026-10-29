class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        k = 0
        for i in sentences:
            count = 1
            for j in i:
                if j==' ':
                    count=count+1
            k = max(count,k)
        return k