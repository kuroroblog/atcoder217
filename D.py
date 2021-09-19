# arrayについて : https://docs.python.org/ja/3/library/array.html
import array
import bisect

# 二分探索を行う関数
def binary_search(a, b):
    min = 0
    max = len(b) - 1
    while min <= max:
        # 中央のインデックスを取得する。
        middle = (min + max) // 2
        if b[middle] == a:
            min = max = middle
            break
        elif b[middle] < a:
            min = middle + 1
        else:
            max = middle - 1
    return [min, max]

# 標準入力を受け付ける。
L, Q = map(int, input().split())

# メモリの使用量を抑えるために、一次元配列のみ & 型制限されるarrayを利用する。
# 参考 : https://note.nkmk.me/python-list-array-numpy-ndarray/
arr = array.array("i", [0, L])

for _ in range(Q):
    # 標準入力を受け付ける。
    c, x = map(int, input().split())
    if c == 1:
        # xから一番近いarrの値 < x < xから一番近いarrの値になるように、xを格納する。
        # bisect.insortについて : https://docs.python.org/ja/3/library/bisect.html#bisect.insort
        bisect.insort(arr, x)
    elif c == 2:
        # 二分探索を利用して、xに近いarr(配列)のインデックス値を取得する。
        # 二分探索とは? : https://e-words.jp/w/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2.html#:~:text=%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E3%81%A8%E3%81%AF%E3%80%81%E3%83%87%E3%83%BC%E3%82%BF,%E3%81%AB%E6%8E%A2%E7%B4%A2%E3%82%92%E8%A1%8C%E3%81%86%E6%89%8B%E6%B3%95%E3%80%82
        minIdx, maxIdx = binary_search(x, arr)
        print(max(arr[minIdx] - arr[maxIdx], arr[maxIdx] - arr[minIdx]))
