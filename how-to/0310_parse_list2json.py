import requests
import json


url = {
    "live":"https://merlion.rcmd.shopee.io/api/bundle-meta",
    "liveish":None
}

def dump_json(custom_workers):
    data = {
        "custom_workers":None,
    }
    if custom_workers:
        data["custom_workers"]=custom_workers

    with open('0310_parse_list2json.json', 'w') as f:
        json.dump(data, f, indent=4)


def fetch_data(url):
    resp = requests.get(url)
    return resp


if __name__ =="__main__":
    
    resp = fetch_data(url["live"])
    objs = json.loads(resp.text)
    
    freq_d = {}
    custom_workers = {}
    for obj in objs:
        data = {
            "key":obj['key'],
            "workers":obj['workers']
        }
        custom_workers[obj['key']] = obj['workers']

        # freq_d[str(obj['workers'])] = freq_d.get(str(obj['workers']),0)+1
        
    
    dump_json(custom_workers)
    print(freq_d)
