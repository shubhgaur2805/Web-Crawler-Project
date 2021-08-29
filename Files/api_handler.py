import requests
import json
import math
import time
from datetime import datetime
from datetime import timedelta
class Api_handler:
    def __init__(self):
        self.token_key = None
        self.time_out = None
        self.get_key = None
        self.get_metadata = {}
        self.all_category = []
        self.token_url="https://public-apis-api.herokuapp.com/api/v1/auth/token"
        self.category_url="https://public-apis-api.herokuapp.com/api/v1/apis/categories?page="
        self.category_name_url="https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=1&category="
        self.page_url="https://public-apis-api.herokuapp.com/api/v1/apis/entry?page="


    def get_token(self):
        token = requests.get(self.token_url)
        curr = datetime.now()
        self.time_out = curr + timedelta(minutes=4.80)
        self.get_key = token.json()
        self.token_key = self.get_key["token"]
        return self.token_key

    def get_categories(self):
        data = requests.get(self.category_url+str(1),
                            headers={"Authorization": "Bearer " + self.token_key})
        for key, value in data.json().items():
            if key == "count":
                get_page = math.ceil(value / 10)
            else:
                for name in value:
                    self.all_category.append(name)
        for i in range(2, get_page + 1):
            data = requests.get(self.category_url + str(i),
                                headers={"Authorization": "Bearer " + self.token_key})
            for key, value in data.json().items():
                if key == "categories":
                    for j in value:
                        self.all_category.append(j)
        return self.all_category

    def reset_token(self):
        print("Reset Server")
        token = requests.get(self.token_url)
        curr = datetime.now()
        self.time_out = curr + timedelta(minutes=4.80)
        self.get_key = token.json()
        self.token_key = self.get_key['token']


    def get_api(self):
        for name in self.all_category:
            # Get Current time
            curr_time = datetime.now()

            # compare and update time
            if self.time_out < curr_time:
                self.reset_token()


            # Get api meta data of page 1
            categories_data = requests.get(
                self.category_name_url + name,
                headers={"Authorization": "Bearer " + self.token_key})
            link_data = categories_data.headers
            self.get_metadata[name] = categories_data.json()["categories"]
            # check for Rate limit
            if int(link_data["X-Ratelimit-Remaining"]) == 0:
                print("Wait for 60 sec")
                time.sleep(60)
            cat_pages = math.ceil(int(categories_data.json()["count"]) / 10)
            count = int(categories_data.json()["count"])

            if count > 10:
                for k in range(2, cat_pages + 1):
                    # Get Current time
                    curr_time = datetime.now()
                    if self.time_out < curr_time:
                       self.reset_token()

                    categories_data = requests.get(self.page_url +
                                                       str(k) + "&category=" + str(name), headers={"Authorization": "Bearer " + self.token_key})
                    link_data = categories_data.headers
                    if int(link_data["X-Ratelimit-Remaining"]) == 0:
                        print("Wait for 60 sec")
                        time.sleep(60)
                    self.get_metadata[name] += categories_data.json()["categories"]
        return self.get_metadata

