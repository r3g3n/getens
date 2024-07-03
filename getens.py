import sys
import requests
import json

def get_ens_name(wallet_address):
    url = f"https://api.chainbase.online/v1/account/ens?chain_id=1&address={wallet_address}"
    headers = {
        "accept": "application/json",
        "x-api-key": "demo"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            names = [item["name"] for item in data["data"]]
            return names
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python getens.py <wallet_address>")
        sys.exit(1)

    wallet_address = sys.argv[1]
    names = get_ens_name(wallet_address)
    if names:
        print("\n".join(names))
