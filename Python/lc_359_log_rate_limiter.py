# Time: O(1) for a particular query
# Space: O(unique messages)

# Can also do O(10) space, that only stores data for last 10 seconds
# But the question suggests we can have multiple elements coming in at roughly
# the same time, "It is possible that several messages arrive roughly at the same time."

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.imap = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        if message not in self.imap:
            self.imap[message] = timestamp
            return True
        else:
            if timestamp>=self.imap[message]+10:
                self.imap[message] = timestamp
                return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
