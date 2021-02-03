import requests

sheet_endpoint = "https://api.sheety.co/1274e5bff0f612a7132ca3098efb8a41/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data= {
                "price": {
                    "IATA COde": city["IATA Code"]
                }
            }

        response = requests.put(url=f"{sheet_endpoint}/{city['id']}", json=new_data)
        print(response.text)

