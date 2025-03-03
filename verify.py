import requests
import time
import hashlib
import hmac
import base64

# Replace these with your actual values
consumer_key = "f36d751c-7a07-4374-b9f1-421c90c24b74"
consumer_secret = "chmaH9m5WsJwXOwCohvgihgZLgRf2Lbsbq4"
request_token = "ce1629f9-2788-49bc-90d4-bec0f9c849ba"
request_token_secret = "p3rzL33lAuA7uDw6LhFuhUjKtWCHgP5N3rt"
oauth_verifier = "VE0MsgHidv"

# Request URL
url = "https://connectapi.garmin.com/oauth-service/oauth/access_token"

# Current timestamp
oauth_timestamp = str(int(time.time()))

# Generate OAuth signature
base_string = "&".join([
    "POST",
    requests.utils.quote(url, safe=''),
    requests.utils.quote('&'.join([
        f"oauth_consumer_key={consumer_key}",
        f"oauth_nonce={oauth_timestamp}",
        "oauth_signature_method=HMAC-SHA1",
        f"oauth_timestamp={oauth_timestamp}",
        f"oauth_token={request_token}",
        f"oauth_verifier={oauth_verifier}",
        "oauth_version=1.0"
    ]), safe='')
])

signing_key = "&".join([requests.utils.quote(consumer_secret, safe=''), requests.utils.quote(request_token_secret, safe='')])

signature = base64.b64encode(hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1).digest()).decode()

# Construct authorization header
authorization_header = ', '.join([
    f'OAuth oauth_nonce="{oauth_timestamp}"',
    f'oauth_signature_method="HMAC-SHA1"',
    f'oauth_timestamp="{oauth_timestamp}"',
    f'oauth_consumer_key="{consumer_key}"',
    f'oauth_token="{request_token}"',
    f'oauth_verifier="{oauth_verifier}"',
    f'oauth_signature="{requests.utils.quote(signature, safe="")}"',
    f'oauth_version="1.0"'
])

# Make the POST request
response = requests.post(url, headers={'Authorization': authorization_header})

# Print the response
print(response.text)
