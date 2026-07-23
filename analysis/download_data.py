import kagglehub
import pandas as pd

# SECOM data
path = kagglehub.dataset_download("paresh2047/uci-semcom")
print(f"Dataset downloaded to: {path}")


# CSET dat
print("Loading CSET Supply Chain Data...\n")

# Load all the supply chain CSV files
try:
    inputs_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/inputs.csv'
    providers_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/providers.csv'
    provision_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/provision.csv'
    stages_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/stages.csv'
    
    df_inputs = pd.read_csv(inputs_url)
    df_providers = pd.read_csv(providers_url)
    df_provision = pd.read_csv(provision_url)
    df_stages = pd.read_csv(stages_url)
    
    print("✅ INPUTS (tools, materials, processes):")
    print(f"   Shape: {df_inputs.shape}")
    print(f"   Columns: {df_inputs.columns.tolist()}\n")
    
    print("✅ PROVIDERS (countries, companies):")
    print(f"   Shape: {df_providers.shape}")
    print(f"   Columns: {df_providers.columns.tolist()}\n")
    
    print("✅ PROVISION (who provides what):")
    print(f"   Shape: {df_provision.shape}")
    print(f"   Columns: {df_provision.columns.tolist()}\n")
    
    print("✅ STAGES (production stages):")
    print(f"   Shape: {df_stages.shape}")
    print(f"   Columns: {df_stages.columns.tolist()}\n")
    
    print("\n📊 Sample data from PROVIDERS:")
    print(df_providers.head())
    
except Exception as e:
    print(f"❌ Error: {e}")