class Solution:
    """
    @param time:
    @return: return a string represents time
    """
    def nextTime(self, time):
        timeSplit = time.split(":")
        if len(time) != 5 or len(timeSplit) != 2:
            return "-1"

        hour = int(timeSplit[0])
        minute = int(timeSplit[1])
        if hour > 23 or minute > 59:
            return "-1"

        while True:
            minute += 1
            if minute == 60:
                minute = 0
                hour = 0 if hour == 23 else hour + 1

            result = "{:02d}:{:02d}".format(hour, minute)
            if len(set(result)) == 5:
                return result