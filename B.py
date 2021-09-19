# 予め、ABC, ARC, AGC, AHCの値をリストへ格納する。
atcoderList = [
    'ABC',
    'ARC',
    'AGC',
    'AHC',
]

# 標準入力を受け付ける。
s1 = input()
s2 = input()
s3 = input()

# S1, S2, S3が入力される度に、上記で作成したリストと合致する値を削除する。
# remove関数参考 : https://note.nkmk.me/python-list-clear-pop-remove-del/
atcoderList.remove(s1)
atcoderList.remove(s2)
atcoderList.remove(s3)

print(atcoderList[0])
