import pandas as pd
import os

df = pd.read_csv("data/raw/events.csv")

df = df.dropna()

df = df[df["event_type"].isin(df["event_type"].unique())]

df = df[df["duration_seconds"] > 0]

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="mixed",
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

os.makedirs("data/clean", exist_ok=True)

df.to_csv("data/clean/events.csv", index=False)
