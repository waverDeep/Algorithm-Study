org_numbers = set(range(1, 10001))
gen_numbers = set()
for number in org_numbers:
    keep = number
    while number > 0:
        keep += int(number % 10)
        number = int(number / 10)
    gen_numbers.add(keep)
self_numbers = sorted(org_numbers-gen_numbers)
for number in self_numbers:
    print(number)