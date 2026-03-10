
import pandas as pd

def build_features():
    orders = pd.read_csv("data/orders.csv")
    products = pd.read_csv("data/products.csv")

    user_features = orders.groupby("user_id").size().reset_index()
    user_features.columns = ["user_id","total_orders"]

    product_features = orders.groupby("product_id").size().reset_index()
    product_features.columns = ["product_id","popularity"]

    user_features.to_csv("data/user_features.csv",index=False)
    product_features.to_csv("data/product_features.csv",index=False)

if __name__ == "__main__":
    build_features()
