class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # nodes of the graph will be (email, name)
        # we will create an adj list that stores all emails

        # build the adj list
        adjList = {}
        for account in accounts:
            name = account[0]
            firstEmailNode = (account[1], name)
            if firstEmailNode not in adjList:
                adjList[firstEmailNode] = set()

            otherEmails = account[2:]
            for otherEmail in otherEmails:
                otherEmailNode = (otherEmail, name)
                adjList[firstEmailNode].add(otherEmailNode)

                # undirected Graph
                if otherEmailNode not in adjList:
                    adjList[otherEmailNode] = set()
                adjList[otherEmailNode].add(firstEmailNode)

        # DFS

        visited = set()
        mergedAccounts = []

        def dfs(node):
            ret = [node]
            visited.add(node)
            for child in adjList[node]:
                if child not in visited:
                    ret = ret + dfs(child)
            return ret

        for node in adjList:
            if node not in visited:
                accounts = dfs(node)
                name = [node[1]]
                currMergedAcc = []
                for account in accounts:
                    currMergedAcc.append(account[0])
                currMergedAcc.sort()
                currMergedAcc = name + currMergedAcc
                mergedAccounts.append(currMergedAcc)
        return mergedAccounts
