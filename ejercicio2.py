import random

print("Generando 100 numeros...")
nums = [random.randint(1, 1000) for _ in range(100)]
print("\nLista Original:")
print(nums)
print("\nLista Inversa:")
print(nums[::-1])
