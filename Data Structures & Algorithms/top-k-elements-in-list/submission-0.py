class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # 辞書を使って出現数をカウントする
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # (出現回数, 数字)のペアを作成する
        freq_list = []
        for num, freq in count.items():
            freq_list.append((freq, num)) # 出現回数を先にするのがポイント
        
        # 出現回数の要素を基準に，大きい順にソート
        freq_list.sort(reverse=True)

        # 上位k個の「数字だけを」結果リストにまとめる
        result = []
        for i in range(k):
            result.append(freq_list[i][1])

        
        return result