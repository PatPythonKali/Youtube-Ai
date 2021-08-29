result = 80
if result >= 60:
    result = str(result / 60)
    result = result[:4] + " Minutes"

print(f"Total Execution Time: {result}")