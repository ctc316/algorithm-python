class Solution:
    """
    @param time:
    @return: return a string represent time
    """
    def lastTime(self, time):
        timeSplit = time.split(":")
        if len(time) != 5 or len(timeSplit) != 2:
            return "-1"

        hour = int(timeSplit[0])
        minute = int(timeSplit[1])
        if hour > 23 or minute > 59:
            return "-1"

        minute -= 1
        if minute < 0:
            minute = 59
            hour = 23 if hour == 0 else hour - 1

        return "{:02d}:{:02d}".format(hour, minute)