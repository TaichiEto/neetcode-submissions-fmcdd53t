class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        # tの文字の出現回数をカウントする
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        window = {} # 今持ってるものリスト：現在、窓の中にある文字の個数を記録する
        have = 0 # 窓の中で、必要な個数を満たした文字の種類数
        need = len(count_t) # 必要な文字の「種類」の数

        # 結果を保存する変数 [最小の長さ, 左インデックス, 右インデックス]
        res_len = float('infinity') # これは誰？ float('infinity')って初めて打ち込んだ気がする。
        res_pos = [-1, -1] # これも誰？

        left = 0
        for right in range(len(s)):
            char_r = s[right]
            window[char_r] = window.get(char_r, 0) + 1

            # 必要な文字が、必要な数だけ窓の中に揃ったら、haveを増やす
            if char_r in count_t and window[char_r] == count_t[char_r]:
                have += 1
            while have == need:
                # 最小値の更新
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_pos = [left, right]

                # 左端の文字を捨てる
                char_l = s[left]
                window[char_l] -= 1
                
                # もし捨てた文字が必要な文字で、かつ足りなくなってしまったら
                if char_l in count_t and window[char_l] < count_t[char_l]:
                    have -= 1 # 条件を満たさなくなるので while を抜ける
                    
                left += 1

        # 結果の文字列を返す（見つからなかった場合は空文字）
        l, r = res_pos
        return s[l:r+1] if res_len != float("infinity") else ""