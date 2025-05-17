

# python program to Use lists and functions.
students = []
while True:
    name = input("Name (or 'done'): ")
    if name == 'done': break
    scores = [float(input(f"Test {i+1}: ")) for i in range(3)]
    students.append((name, round(sum(scores)/3, 2)))

print("\nReport:")
for name, avg in students:
    print(f"{name}: {avg}")
