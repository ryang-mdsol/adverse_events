import os
import snowflake.connector

# Snowflake configuration
config = {
    'account': 'vaa16628.us-east-1',
    'user': os.getenv('USER'),
    'warehouse': 'ACORN_DSE_PROD_VW',
    'database': 'ACORN_DSE_UAT_DATA_MART_CLN',
    'schema': 'AE_PREDICTION',
    'role': 'ACORN_DSE_AE_PREDICTION'
}

# Connect to Snowflake - connector handles the key conversion automatically
ctx = snowflake.connector.connect(
    account=config['account'],
    user=config['user'],
    warehouse=config['warehouse'],
    database=config['database'],
    schema=config['schema'],
    role=config['role'],
    authenticator='SNOWFLAKE_JWT',
    private_key_file=os.getenv('snowflake_key_path')
)

# Run query
query = "SELECT * FROM requested_forms LIMIT 10"
cur = ctx.cursor()
cur.execute(query)
df = cur.fetch_pandas_all()

print(f"Loaded {len(df)} rows")
print(df.head())

# Close connection
ctx.close()
