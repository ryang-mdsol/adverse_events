from src.connection_snowflake import snowflake_connect_and_load

# Configuration for ae_prediction table
config = {
    'account': 'vaa16628.us-east-1',
    'warehouse': 'ACORN_DSE_PROD_VW',
    'database': 'ACORN_DSE_UAT_DATA_MART_CLN',
    'schema': 'AE_PREDICTION',
    'role': 'ACORN_DSE_AE_PREDICTION'
}

# Simple test query
query = "SELECT * FROM requested_forms LIMIT 10"

# Load data
df = snowflake_connect_and_load(config, query)

print(f"Loaded {len(df)} rows")
print(df.head())
