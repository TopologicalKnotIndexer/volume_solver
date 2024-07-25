import sys
from volume_solver import get_volume

def main():
    inp = eval(sys.stdin.read()) # 不做检查，假设他是一个合法的 hyperbolic knot
    print(get_volume(inp))

if __name__ == "__main__":
    main()