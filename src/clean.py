import os
import pandas as pd

os.makedirs("data/clean", exist_ok=True)

df = pd.read_csv("data/raw/events.csv")

df = df.dropna()
df = df[~df.eq("").any(axis=1)]

df["event_type"] = df["event_type"].astype(str).str.lower().str.strip()

valid_event_types = {"click", "login", "purchase", "scroll", "view"}
df = df[df["event_type"].isin(valid_event_types)]

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df[df["duration_seconds"].notna()]
df = df[df["duration_seconds"] > 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df[df["timestamp"].notna()]
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

df.to_csv("data/clean/events.csv", index=False)
