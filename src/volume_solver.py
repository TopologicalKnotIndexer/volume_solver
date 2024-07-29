# 如何处理超时机制
# https://stackoverflow.com/questions/492519/timeout-on-a-function-call
# works on Unix Like OS
import signal

from snappy     import Manifold
from to_dt_code import to_dt_code

EPS = 1e-5

def raw_get_volume(pd_code: list) -> float:
    manifold = Manifold("DT:[%s]" % str(to_dt_code(pd_code)))
    return float(manifold.with_hyperbolic_structure().volume())

def get_volume(pd_code) -> float|str: # 计算扭结补空间体积
    ans = 0.000
    try:
        ans = raw_get_volume(pd_code)
    except:
        pass
    if abs(ans) < EPS: # 2024-07-30 又把这个判断加回来了
        ans = 0.000
    assert ans >= 0
    return max(ans, 0.000) # 当计算出错时，返回 0.000

if __name__ == "__main__":
    print(get_volume([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))
    print(get_volume([[2, 8, 3, 7], [4, 10, 5, 9], [6, 2, 7, 1], [8, 4, 9, 3], [10, 6, 1, 5]]))
    print(get_volume([[1, 9, 2, 8], [3, 11, 4, 10], [5, 13, 6, 12], [7, 1, 8, 14], [9, 3, 10, 2], [11, 5, 12, 4], [13, 7, 14, 6]]))
    print(get_volume([[2, 14, 3, 13], [5, 11, 6, 10], [7, 15, 8, 14], [9, 5, 10, 4], [11, 7, 12, 6], [12, 2, 13, 1], [15, 9, 16, 8], [16, 4, 1, 3]]))
    print(get_volume([[1, 11, 2, 10], [3, 13, 4, 12], [5, 15, 6, 14], [7, 17, 8, 16], [9, 1, 10, 18], [11, 3, 12, 2], [13, 5, 14, 4], [15, 7, 16, 6], [17, 9, 18, 8]]))
    print(get_volume([[4, 2, 5, 1], [15, 22, 16, 1], [10, 3, 11, 4], [2, 11, 3, 12], [9, 17, 10, 16], [7, 19, 8, 18], [17, 9, 18, 8], [19, 13, 20, 12], [5, 14, 6, 15], [13, 21, 14, 20], [21, 7, 22, 6]]))
