# 937. Reorder Log Files
# Time: O(len(logs)*log(len(logs)))
# Space: O(len(logs))

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        num_logs = []
        let_logs = []

        for log in logs:
            words = log.split()

            if words[1].isdigit():
                num_logs.append(log)
            else:
                let_logs.append(log)

        let_logs = sorted(let_logs, key = lambda log: (log.split()[1:],log.split()[0]))

        return let_logs+num_logs
