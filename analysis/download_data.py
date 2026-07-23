import kagglehub
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Then your code
inputs_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/inputs.csv'
df_inputs = pd.read_csv(inputs_url)

# SECOM data
path = kagglehub.dataset_download("paresh2047/uci-semcom")
print(f"Dataset downloaded to: {path}")


# CSET dat
print("Loading CSET Supply Chain Data...\n")

# Load all the supply chain CSV files w/ exception error
try:
    inputs_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/inputs.csv'
    providers_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/providers.csv'
    provision_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/provision.csv'
    stages_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/stages.csv'
    
    df_inputs = pd.read_csv(inputs_url)
    df_providers = pd.read_csv(providers_url)
    df_provision = pd.read_csv(provision_url)
    df_stages = pd.read_csv(stages_url)
    
except Exception as e:
    print(f"❌ Error: {e}")