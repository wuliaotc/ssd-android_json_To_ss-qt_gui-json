import json


def convert(file: str):

    configs = []
    w = open('gui-config.json', 'w+')
    with open(file) as f:
        data = json.load(f)
        for item in data:
            if '游' in item['remarks'] or '回国' in item['remarks'] or '韩' in item['remarks']:#排除游戏线路
                continue
            if '港专' not in item['remarks'] and '日专' not in item['remarks'] and '湾' not in item['remarks']:
                continue
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
