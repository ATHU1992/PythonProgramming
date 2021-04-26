from pathlib import Path

path = Path("ecommerce")
print(path.exists())

path = Path("emails")
print(path.mkdir())

path = Path("emails")
print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)

path = Path()
print(path.glob('*'))