import pandas as pd


# CSVファイルの読み込みと保存
def load_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["元の単語", "置き換え後の単語", "タグ", "属性"])

def save_csv(df, filename):
    df.to_csv(filename, index=False)

# 状態管理クラス
class StateManager:
    def __init__(self):
        self.history = []  # 状態の履歴を保存するリスト

    def save_state(self, df):
        # 現在のデータフレームのコピーを履歴に追加
        self.history.append(df.copy())

    def undo(self):
        # 1つ前の状態に戻す（履歴から最新の状態を削除）
    
        if len(self.history) > 1:
            self.history.pop()
        return self.history[-1].copy() if self.history else None
    
    def history_count(self):
        if len(self.history)==1 :
            return 1
        else:
            return len(self.history)
    
    def clear(self):
        self.history=[]



