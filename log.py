import math

print("Number (x)\tlog₂(x)")
print("-" * 20)

for i in range(1, 17):
  try:
    log_value = math.log2(i)
    print(f"{i}\t\t{log_value:.4f}")
  except ValueError:
    print(f"{i}\t\tError: Math domain error")
