class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # 「文字数 + "#" + 文字列」の形でくっつける
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        # 読み込み開始位置のポインタ
        i = 0
        while i < len(s):
            j = i
            # 1. "#"がくるまでjをすすめて，文字列の部分を特定する．
            while s[j] != "#":
                j += 1
            # 2. "#"の手前までが文字数なので，intに変換する
            length = int(s[i:j])
            # 3. "#"の次の文字から，lengthの部分だけ切り取る
            word = s[j+1:j+1+length]
            res.append(word)
            # 4. ポインタiを，次の単語のスタート位置まで飛ばす
            i = j + 1 + length
        return res