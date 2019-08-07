import json


def convert(file: str):
    """
        "method": "aes-256-cfb",
        "password": "sKT3e0",
        "remarks": "ssrcloud%20-%20%E4%B8%AD%E6%B8%AF%E4%B8%93%E7%BA%BF%20IPLC%20D1%201000Mbps%202%E5%80%8D",
        "server": "sg21.bilibilivpn.com",
        "server_port": 2079
    """
    configs = []
    w = open('gui-config1.json', 'w+')
    with open(file) as f:
        data = json.load(f)
        for item in data:
            configs.append({
                "method": item["method"],
                "password": item["password"],
                "remarks": item["remarks"],
                "server": item["server"],
                "server_port": item["server_port"]
            })

    json.dump({'configs': configs, "localPort": 1080, "shareOverLan": 'false'}, w, indent=4,ensure_ascii=False)
    w.close()


if __name__ == "__main__":
    convert("profiles.json")
