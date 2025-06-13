import argparse
import json
import requests

METADATA_BASE_URL = "http://169.254.169.254/latest"

def get_token():
    """Get a session token for IMDSv2."""
    try:
        response = requests.put(
            f"{METADATA_BASE_URL}/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=2
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error getting token: {e}")
        return None

def get_metadata(path, token):
    """Get metadata for a specific path."""
    url = f"{METADATA_BASE_URL}/meta-data/{path}"
    headers = {"X-aws-ec2-metadata-token": token}
    try:
        response = requests.get(url, headers=headers, timeout=2)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def main():
    metadata_paths = {
        "instance-id": "instance-id",
        "instance-type": "instance-type",
        "ami-id": "ami-id",
        "hostname": "hostname",
        "local-ipv4": "local-ipv4",
        "public-ipv4": "public-ipv4",
        "availability-zone": "placement/availability-zone",
        "security-groups": "security-groups"
    }

    parser = argparse.ArgumentParser(description="Fetch EC2 instance metadata.")
    for key in metadata_paths.keys():
        parser.add_argument(f"--{key}", action="store_true", help=f"Return {key}")

    args = parser.parse_args()
    token = get_token()
    if not token:
        return

    if any(vars(args).values()):
        # User requested specific keys
        result = {}
        for key, path in metadata_paths.items():
            if getattr(args, key.replace('-', '_')):
                value = get_metadata(path, token)
                if value is not None:
                    result[key] = value
        print(json.dumps(result, indent=2))
    else:
        # Default: return all metadata
        result = {}
        for key, path in metadata_paths.items():
            value = get_metadata(path, token)
            if value is not None:
                result[key] = value
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

