import itertools

def get_combinations(data):
  """Returns all possible combinations of the specified data."""
  combinations = []
  for i in range(len(data)):
    for j in range(i + 1, len(data) + 1):
      combinations.append(list(itertools.combinations(data, j)))
  return combinations

if __name__ == "__main__":
  data = input("Enter the data: ")
  data = data.split()
  combinations = get_combinations(data)
  for combination in combinations:
    print(" ".join(combination))
