
import math


def square_root(x):
    y = math.sqrt(x)
    return y
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto