import pandas as pd

df = pd.read_csv("../dataset/movies.csv")
print(df[df["title"] == "Avengers: Infinity War"])
