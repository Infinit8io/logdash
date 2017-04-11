from psutil_fetching import psutil_fetching
import requests

def main():
    # Getting the JSON log
    log = psutil_fetching()

    # POST the log on flask app
    r = requests.post("http://localhost:5000/consume", json=log)

    # Print status code and response
    print(r.status_code)
    print(r.json)

if __name__ == "__main__":
    main()
