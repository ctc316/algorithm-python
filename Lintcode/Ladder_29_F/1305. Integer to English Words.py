class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """

    num_table = {0: 'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
    unit_table = {1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'}

    def numberToWords(self, num):
        if num <= 20:
            return self.num_table[num]

        result = ""
        count = 0
        while num > 0:
            if count > 0:
                result = self.unit_table[count] + " " + result
            result = self.handle_3_digits(num % 1000) + " " + result
            num = int(num / 1000)
            count += 1

        return result.strip()


    def handle_3_digits(self, num):
        result = ""
        if num >= 100:
            result += str(self.num_table[int(num/100)]) + " " + "Hundred"

        result += " " + self.tens_digits(num % 100)

        return result.strip()


    def tens_digits(self, num):
        if num <= 20 or num % 10 == 0:
            return str(self.num_table[num])

        return str(self.num_table[num - num % 10]) + " " + str(self.num_table[num % 10])