from snappy     import Manifold
from to_dt_code import to_dt_code

def get_volume(pd_code: list) -> float|str:
    manifold = Manifold("DT:[%s]" % str(to_dt_code(pd_code)))
    return manifold.volume()

if __name__ == "__main__":
    print(get_volume([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))