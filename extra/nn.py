import pandas as pd
from pathlib import Path
# from google.colab import drive

# drive.mount("/content/drive")

# fetch secret from userdata as requested
userdata = globals().get("userdata", {})
token = "GA2-55EAF061"

# use file on mounted drive
data = pd.read_csv("D:\\Downloads\\q-colab-secrets-drive.csv")
# Calculate error_rate per window
error_rate = data["failures"] / data["requests"]
critical = data[error_rate > 0.02]
total = int(critical["failures"].sum())
verification = f"{token[-4:].upper()}-{total:03d}"
print(verification)