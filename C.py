# 標準入力を受け付ける。
N = int(input())
P = list(map(int, input().split()))

Qinfo = []
for i in range(0, N):
    # 順列Qを作成するために、pi番目とiの関係を紐づける。
    Qinfo.append({
        'index': P[i],
        'position': i + 1,
    })

# piをソートする。
# key optionについて : https://note.nkmk.me/python-key-sort-sorted-max-min/
Qinfo = sorted(Qinfo, key=lambda x:x['index'])

ans = ''
# Qを出力する。
for i in range(0, N):
    ans += str(Qinfo[i]['position']) + ' '

print(ans)
