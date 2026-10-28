import requests

HEADERS = {"User-Agent":"BooksPipeline/1.0 (contact: saidhjji7@gmail.com)"}

def get_html(url):
    session = requests.Session()
    session.headers.update(HEADERS)

    try:
        reponse = session.get(url , timeout=10)
        reponse.raise_for_status()

        return reponse.text
    except requests.RequestException as e:
        print(f"erreur {e}")
        return None


