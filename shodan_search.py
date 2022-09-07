import shodan

from urllib.parse import urlparse


def connect_host_to_ip(api_key: str, query: str):
    api = shodan.Shodan(api_key)
    output = {
        "amount": 0,
        "results": [],
        "error": ""
    }
    try:
        results = api.search(query)

        output["amount"] = results['total']
        for result in results['matches']:
            ip = result['ip_str']
            headers = result["data"].split("\n")
            for header in headers:
                if "Location: " in header:
                    location_header = header.strip().replace("Location: ", "")
            domain = urlparse(location_header).netloc
            output["results"].append({
                "ip": ip,
                "domain": domain
            })
    except shodan.APIError as e:
        output["error"] = e

    return output
