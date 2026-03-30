class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace("!", "")
        s = s.replace(",", "")
        s = s.replace(".", "")
        s = s.replace("'", "")
        s = s.replace(";", "")
        s = s.replace(":", "")
        s = s.replace("/", "")
        s = s.replace("@", "")
        s = s.replace("`", "")
        s = s.lower()

        if s == s[::-1]:
            return True
        else:
            return False