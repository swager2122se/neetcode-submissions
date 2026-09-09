class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # [""] = [[""]]
        # ["a"] = [["a"]]
        #["ab","ba"] = [["ab,ba"]]

        myMap = defaultdict(list)

        for word in strs:
            # Sort the characters and join them to form a valid dictionary key
            sortedWord = "".join(sorted(word))
            # defaultdict automatically creates a new list if the key is missing
            myMap[sortedWord].append(word)
        
        # Return just the grouped lists, not the dictionary keys
        return list(myMap.values())