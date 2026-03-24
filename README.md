# adverse_events
Repository to load and analyze adverse event data

---

## Set-up snowflake authentication

1. Create key-pair following [Snowflake's instructions](https://docs.snowflake.com/en/user-guide/key-pair-auth)

2. Add environment variables to `~/.bashrc`:
   ```bash
   export snowflake_key_path=<path to where the rsa_key.p8 is stored>
   export snowflake_key_pass=''
   ```

3. Run the setup script:
   ```bash
   python src/snowflake/create_snowflake_key.py
   ```

4. Add the key from the terminal into `~/.bashrc`:
   ```bash
   export snowflake_private_key=<key from previous step>
   ```