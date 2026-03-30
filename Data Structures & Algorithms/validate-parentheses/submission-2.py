class Solution:
    def isValid(self, s: str) -> bool:
        # 開きカッコを積むためのスタック（ただのリスト）
        stack = []
        
        # Taichiさんのアイデアを少し最適化。
        # 「閉じカッコ」をキーにして、「開きカッコ」を値にしておくと後の判定が楽になります。
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # もし「閉じカッコ」が来た場合
                # スタックが空ならダミー文字 '#' を入れ、空じゃなければ一番上を取り出す
                top_element = stack.pop() if stack else '#'
                
                # 取り出した「開きカッコ」が、辞書で定義した正しいペアと違ったらアウト
                if mapping[char] != top_element:
                    return False
            else:
                # もし「開きカッコ」が来た場合、問答無用でスタックに積む
                stack.append(char)

        # 最後まで判定して、スタックが空っぽ（全部ペアになって消化された）ならTrue
        return not stack