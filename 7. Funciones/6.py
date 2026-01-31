def media(numbers):
	if not numbers:
		return 0
	return sum(numbers) / len(numbers)

sample = [10, 20, 30, 40, 50]
print(f"Media: {media(sample)}")