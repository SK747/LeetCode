class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        print(s)
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        print(s)
        for char in s:
            number += translations[char]
            print(char,translations[char])
        return number

s = Solution()
print(s.romanToInt('XIV'))

popneed_simple_clothing
popneed_crude_items = []
popneed_basic_food = []
popneed_heating = []
popneed_household_items = []
popneed_standard_clothing = []
popneed_services = []
popneed_intoxicants = []
popneed_luxury_drinks = []
popneed_free_movement = []
popneed_communication = []
popneed_luxury_food = []
popneed_luxury_items = []
popneed_art = []