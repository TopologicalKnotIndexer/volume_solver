import os
import shlex
from subprocess import Popen, PIPE
from snappy     import Manifold
from threading import Timer
PYTHON3_PATH = "python3"
DIRNOW       = os.path.dirname(os.path.abspath(__file__))
EXECFILE     = os.path.join(DIRNOW, "main.py")
TIMEOUT      = 15 # 15s to timeout

def run(cmd, inp:str, timeout_sec) -> float|str:
    proc  = Popen(shlex.split(cmd), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    timer = Timer(timeout_sec, proc.kill)
    ans   = "non_hyperbolic"
    try:
        timer.start()
        stdout, stderr = proc.communicate((inp + "\n").encode("utf-8"))
        ans = stdout.decode().strip()
    finally:
        timer.cancel()
    if ans == "": # 处理程序检测到异常的情况
        ans = "non_hyperbolic"
    if ans != "non_hyperbolic": # 试图将浮点数信息还原出来
        ans = float(ans)
    return ans

def get_volume_safe(pd_code:list) -> float|str:
    return run('"%s" "%s"' % (PYTHON3_PATH, EXECFILE), str(pd_code), TIMEOUT)

if __name__ == "__main__":
    print(get_volume_safe([[4, 2, 5, 1], [8, 6, 1, 5], [6, 3, 7, 4], [2, 7, 3, 8]]))
    print(get_volume_safe([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))
    print(get_volume_safe([[4, 2, 5, 1], [15, 22, 16, 1], [10, 3, 11, 4], [2, 11, 3, 12], [9, 17, 10, 16], [7, 19, 8, 18], [17, 9, 18, 8], [19, 13, 20, 12], [5, 14, 6, 15], [13, 21, 14, 20], [21, 7, 22, 6]]))