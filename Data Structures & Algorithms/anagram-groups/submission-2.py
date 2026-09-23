class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(len(strs))
        alphabet = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
        for i in range(101):
            for j in range(len(strs)):
                if len(strs[j]) >= i + 1:
                    alphabet[strs[j][i]].append(j)

        possible = [''] * len(strs)
        for k, v in alphabet.items():      
            for idx in v:
                possible[idx] += k
            
        possibleDict = {} 
        for i in range(len(possible)):
            if possible[i] not in possibleDict:
                possibleDict[possible[i]] = [strs[i]]
            else:
                possibleDict[possible[i]].append(strs[i])
        
        return list(possibleDict.values())

