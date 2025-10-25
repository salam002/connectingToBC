import requests
import json

PINATA_API_KEY = "9ffee340ad242ba23fb4"
PINATA_SECRET_API_KEY = "08dcdbf9e7a53f3299172f56a4d28d254996fdbd97fad0f55aea8b2c447253e9"

def pin_to_ipfs(data):
    assert isinstance(data,dict),f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE

    # need to store data (JSON) on IPFS --> return the CID of the data stored

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {"Content-Type" : "application/json",
               "pinata_api_key":PINATA_API_KEY,
               "pinata_secret_api_key":PINATA_SECRET_API_KEY}
    
    response = requests.post(url, headers=headers, data=json.dumps(data))

    cid = response.json()["IpfsHash"]
    
    return cid 

def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE

    gateway_url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(gateway_url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch from IPFS: {response.status_code} {response.text}")
    
    if content_type == "json":
        data = response.json()

    else:
        data = response.text
    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data


