class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r = r + str(len(s))+ "#" + s
        print(r)
        return r


    def decode(self, s: str) -> List[str]:
        i = 0
        num = ""
        word = False
        r = []
        while i < len(s) + 1:
            print("run")
            if i == len(s) and s[len(s) - 2:len(s)] == "0#":
                r.append("")
                break
            if i == len(s):
                break
            if word is False:
                if s[i] != "#":
                    num = num + s[i]
                else:
                    print(num)
                    word = True
                i = i + 1
            else:
                r.append(s[i:i + int(num)])
                i = i + int(num)
                num = ""
                word = False
        return r
