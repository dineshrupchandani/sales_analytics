import requests
import pandas as pd
BASE_URL = "https://fakestoreapi.com/products"


def fetch_all_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return pd.DataFrame(response.json())

    else:
        print(f"error {response.status_code}, {response.text}")



# Example usage
prod_df = fetch_all_products()
print(prod_df)

prod_df.to_csv("./raw/products_dummy.csv",index=False)

