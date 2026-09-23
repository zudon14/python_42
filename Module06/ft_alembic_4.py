import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="", flush=True)
# Intentional error: create_earth is not exposed by alchemy/__init__.py
# (mypy also reports it on purpose).
print(f"{alchemy.create_earth()}")
