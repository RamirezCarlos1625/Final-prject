import pandas as pd


def load_events(filename):
    """Load a CSV file of event logs into a DataFrame."""
    return pd.read_csv(filename)
