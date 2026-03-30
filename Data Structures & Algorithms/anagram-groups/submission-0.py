import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 親玉の辞書（グループ分け用）
        # キーが無い時は勝手にリスト [] を作ってくれる便利機能
        anagram_map = collections.defaultdict(list)

        for s in strs:
            # 1. 衛藤さんがやりたかった「各単語ごとの文字カウント」
            count_dict = {}
            for char in s:
                count_dict[char] = count_dict.get(char, 0) + 1
            
            # 2. 【魔法】辞書の中身をアルファベット順に並び替えて、変更不可の「タプル」にする！
            # 例: {'c': 1, 'a': 1, 't': 1} -> (('a', 1), ('c', 1), ('t', 1))
            # これで、親玉の辞書の「キー（鍵）」として使えるようになります！
            dna_key = tuple(sorted(count_dict.items()))
            
            # 3. 親玉の辞書に、元の単語を放り込む
            anagram_map[dna_key].append(s)
            
        # 最後にグループ化されたリストたちだけを返す
        return list(anagram_map.values())