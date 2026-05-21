import marimo as mo

app = mo.App()

@app.cell
def imports():
    import pandas as pd
    import matplotlib.pyplot as plt
    return pd, plt


@app.cell
def load(pd):
    df = pd.read_csv("data/features/events.csv")
    return df


@app.cell
def plot(df, plt):
    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"])
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Event Durations")
    return fig


if __name__ == "__main__":
    app.run()
