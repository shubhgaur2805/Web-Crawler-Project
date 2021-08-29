import api_handler
import api_database
def main():
    meta_data=api_handler.Api_handler()
    meta_data.get_token()
    meta_data.get_categories()
    data=meta_data.get_api()
    put_data = api_database.Api_database(data)
    put_data.database()
    put_data.excel()
main()
