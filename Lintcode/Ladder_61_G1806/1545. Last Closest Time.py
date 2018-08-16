class Solution:
    """
    @param time:
    @return: return a string represent time
    """
    def lastTime(self, time):
        if len(time) != 5:
            return "-1"

        timeSplit = time.split(":")
        if len(timeSplit) != 2:
            return "-1"

        minute = int(timeSplit[0])
        second = int(timeSplit[1])

        if minute > 23 or second > 59:
            return "-1"

        second -= 1
        if second < 0:
            second = 59
            minute -= 1

        if minute < 0:
            minute = 23

        return str(minute).zfill(2) + ":" + str(second).zfill(2)