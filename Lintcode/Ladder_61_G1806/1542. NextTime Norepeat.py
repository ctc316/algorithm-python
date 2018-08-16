class Solution:
    """
    @param time:
    @return: return a string represents time
    """
    def nextTime(self, time):
        timeSplit = time.split(":")
        if len(time) != 5 or len(timeSplit) != 2:
            return "-1"

        minute = int(timeSplit[0])
        second = int(timeSplit[1])

        if minute > 23 or second > 59:
            return "-1"

        while True:
            second += 1
            if second == 60:
                second = 0
                minute += 1

            if minute == 24:
                minute = 0

            digit1 = int(minute / 10)
            digit2 = minute % 10
            digit3 = int(second / 10)
            digit4 = second % 10
            if digit1 != digit2 and digit1 != digit3 and digit1 != digit4 and \
               digit2 != digit3 and digit2 != digit4 and digit3 != digit4:
                   return str(digit1) + str(digit2) + ":" + str(digit3) + str(digit4)