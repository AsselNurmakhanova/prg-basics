import json
with open("euro.json", "r") as file:
    data = json.load(file)
print("Date            Buying Rate     Selling Rate")
print("============================================")
for rate in data["rates"]:
    date = rate["effectiveDate"]
    bid = rate["bid"]
    ask = rate["ask"]
    print(f"{date}      {bid:.4f}          {ask:.4f}")
