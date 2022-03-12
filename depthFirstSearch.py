graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

list_run_dfs = []


def dfs(graph, iter):
    if len(graph[iter]) > 0:
        for x in graph[iter]:
            if x not in list_run_dfs:
                list_run_dfs.append(x)
                dfs(graph, x)
            else:
                pass
    else:
        pass


dfs(graph, '5')
print(list_run_dfs)
