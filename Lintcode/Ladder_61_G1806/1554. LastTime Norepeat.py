class Solution:
    """
    @param time:
    @return: return a string represents time
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

        while True:
            second -= 1
            if second < 0:
                second = 59
                minute -= 1

            if minute < 0:
                minute = 23

            digit1 = int(minute / 10)
            digit2 = minute % 10
            digit3 = int(second / 10)
            digit4 = second % 10

            if digit1 != digit2 and digit1 != digit3 and digit1 != digit4 and \
               digit2 != digit3 and digit2 != digit4 and digit3 != digit4:
                   return str(minute).zfill(2) + ":" + str(second).zfill(2)