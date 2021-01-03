import grpc
from grpc_generated_files import calculator_pb2,calculator_pb2_grpc


# Step 1: Create a Channel
channel = grpc.insecure_channel('localhost:80')

# Step 2: Create a Stub
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Step 3: call API
number = calculator_pb2.Number(value=16)
response = stub.SquareRoot(number)
print(response.value)
