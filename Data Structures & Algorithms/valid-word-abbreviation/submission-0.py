class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ab_counter, word_counter = 0, 0

        while ab_counter < len(abbr) and word_counter < len(word):
            if abbr[ab_counter].isalpha():
                if abbr[ab_counter] != word[word_counter]:
                    return False
                ab_counter += 1
                word_counter += 1
            else:
                if abbr[ab_counter] == '0':
                    return False
                num = 0
                while ab_counter < len(abbr) and abbr[ab_counter].isdigit():
                    num = num * 10 + int(abbr[ab_counter])
                    ab_counter += 1
                word_counter += num
        return ab_counter == len(abbr) and word_counter == len(word)