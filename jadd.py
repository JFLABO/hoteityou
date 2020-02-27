import json

def append_json_to_file(data: dict, path_file: str) -> bool:
    with open(path_file, 'ab+') as f:              # ファイルを開く
        f.seek(0,2)                                # ファイルの末尾（2）に移動（フォフセット0）  
        if f.tell() == 0 :                         # ファイルが空かチェック
            f.write(json.dumps([data]).encode())   # 空の場合は JSON 配列を書き込む
        else :
            f.seek(-1,2)                           # ファイルの末尾（2）から -1 文字移動
            f.truncate()                           # 最後の文字を削除し、JSON 配列を開ける（]の削除）
            f.write(' , '.encode())                # 配列のセパレーターを書き込む
            f.write(json.dumps(data).encode())     # 辞書を JSON 形式でダンプ書き込み
            f.write(']'.encode())                  # JSON 配列を閉じる
    return f.close() # 連続で追加する場合は都度 Open, Close しない方がいいかもimport json

PATH_FILE = 'data/test.txt'

#for i in range(10):
#    key  = 'key{num}'.format(num=i)
#    data = { key: i }                    # サンプル辞書データ
#    append_json_to_file(data, PATH_FILE) # 要素を追加
data={"title":"うめきちとうめこ","body":"松本さん 10日で卵を産む","amount":"8000","date":"2020/02/17 12:00"}
append_json_to_file(data, PATH_FILE)
# 検証（保存ファイルのまるごと読み込み）
f_saved  = open(PATH_FILE, "r")
contents = f_saved.read()
f_saved.close()
print(contents)