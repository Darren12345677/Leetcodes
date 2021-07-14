class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        work_list = list(digits)
        master = {'2':['a','b', 'c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],\
                  '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        def combine(lst1, lst2):
            if not lst1:
                return lst2
            elif not lst2:
                return lst1
            result = set()
            for i in lst1:
                for j in lst2:
                    result.add(i+j)
            return list(result)
        result = []
        for i in work_list:
            result = combine(result, master[i])
        return result    