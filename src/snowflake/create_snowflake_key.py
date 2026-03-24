import os
import base64


if __name__ == "__main__":
    fp = os.getenv('snowflake_key_path')
    with open(fp, "r") as f:
        sf_pk_str = f.read()
    bytes_data = sf_pk_str.encode('ascii')
    encoded_data = base64.b64encode(bytes_data)
    encoded_string = encoded_data.decode('utf-8')
    print('encoded_string to use as environment variable snowflake_private_key\n\n\n',encoded_string)