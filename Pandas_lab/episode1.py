import os
import pandas as pd

folder = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(folder, "transactions.csv"))

paid = data[data["STATUS"] == "OK"]

print("3 самых крупных платежа:")
print(paid.nlargest(3, "SUM")[["CONTRACTOR", "SUM"]].to_string(index=False))

total = paid.loc[paid["CONTRACTOR"] == "Umbrella, Inc", "SUM"].sum()
print("Сумма платежей Umbrella, Inc:", total)
