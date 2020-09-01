import json

with open("../secrets.json") as f:
    secrets = json.loads(f.read())


def get_secrets(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError as e:
        error_msg = f"Set {setting} environment variable."
        raise KeyError(error_msg)
