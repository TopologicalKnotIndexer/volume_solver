# volume_solver
给定 PD_CODE 计算扭结补空间体积（只对 hyperbolic knot 有效）。



## 前置条件

- `python3`
- `sage`
- `python3 -m pip install --upgrade --user snappy`



## 使用方式

- `python3 ./src/main.py`
  - 向标准输入流输入一个合法的 PD_CODE （程序不对合法性进行检查）
  - 如果扭结是 hyperbolic knot，则程序向标准输出流输出一个扭结补空间的体积（如果不是 hypobolic 扭结程序，程序输出 `non_hyperbolic`）

