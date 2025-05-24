class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scoresDict = {}
        for match in matches:
            winner, loser = match
            if winner not in scoresDict:
                scoresDict[winner] = [0, 0]
            scoresDict[winner][0] += 1
            if loser not in scoresDict:
                scoresDict[loser] = [0, 0]
            scoresDict[loser][1] += 1
        
        answer = [[],[]]
        for key, value in scoresDict.items():
            if value[1] == 0:
                answer[0].append(key)
                continue

            if value[1] == 1:
                answer[1].append(key)
                continue
        answer[0].sort()
        answer[1].sort()
        return answer