import re
text = "My first phone number: 8777-777-7777, second: 8777-666-6666."

found = re.search(r'\d{4}-\d{3}-\d{4}', text)
print(found.group()) # 8777-777-7777

all_finds = re.findall(r'\d{4}-\d{3}-\d{4}', text)
print(all_finds) # ['8777-777-7777', '8777-666-6666']

parts = re.split(r'\d{4}-\d{3}-\d{4}', text)
print(parts) # ['My first phone number: ', ', second: ', '.']

censored = re.sub(r'\d{4}-\d{3}-\d{4}', '[?]',text)
print(censored) # My first phone number: [?], second: [?].


print()
print()

line = "fruit: apple, cost: 2.5, amount: 5"
price_pattern = r'(\d+\.?\d*)'

price = re.search(price_pattern, line)
if price:
    print("found:", price.group(1))

quantity_pattern = r"amount:\s*(\d+)"
quantity = re.search(quantity_pattern, line)
if quantity:
    print(quantity.group(1))