# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        # 最初は「社長フロア」のリストからスタート
        current_floor = [root] 
        
        # 今のフロアに誰かがいる限りループを続ける
        while current_floor:
            current_values = [] # 今のフロアにいる人の「名前（値）」メモ
            next_floor = []     # 次のフロアにいる「部下」を集める待合室
            
            # 今のフロアにいる全員に対して順番に処理をする
            for node in current_floor:
                # 1. 自分の名前をメモに書く
                current_values.append(node.val)
                
                # 2. 自分の左の部下がいれば、次のフロアの待合室に入れる
                if node.left:
                    next_floor.append(node.left)
                # 3. 自分の右の部下がいれば、次のフロアの待合室に入れる
                if node.right:
                    next_floor.append(node.right)
            
            # 今のフロアの全員分の処理が終わったら、結果リストにメモを綴じる
            result.append(current_values)
            
            # ★ここがポイント！★
            # 次のフロアの待合室にいた人たちを、丸ごと「今のフロア」に昇格させる
            current_floor = next_floor 
            
        return result