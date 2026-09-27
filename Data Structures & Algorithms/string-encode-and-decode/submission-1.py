class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for item in strs:
            encoded += item + "\\c\\c"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        cur_str = ""
        i = 0

        while i < len(s):
            if s[i] == "\\" and s[i+1] == "c" and s[i+2] == "\\" and s[i+3] == "c": 
                decoded_strs.append(cur_str)
                cur_str = ""
                i = i+4
            else:
                cur_str += s[i]
                i += 1

        return decoded_strs