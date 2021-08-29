# Postman_Assigment
### Project - Get metadata from API and store in a database. 
#### Given  -  POSTMAN API 
## Step to run a code:
    - You just pull all files from the repository
    - You will get 5 files in the downloaded folder
    - Execute cmd Python main.py (Make sure Python should be installed on your system) 
    - you will get the output: api_database.db and a csv_file as Data
## Details of all the tables and their schema:
    There is Two tables in the database: -
	Table 1: Api_metadata has all metadata of API's
		 - It contain metadata S_No, API_name, Description, Auth, HTTPS, Cors, Link, Category_ID.
		 - S_No is a primary key.
		 - Category_ID is a Forigen key.
		 
   	Table 2: Api_category has a category's of API
		 - It contain ID, Category
		 - ID is Primary key.

### Database Schema:
![new_1](https://user-images.githubusercontent.com/65850757/131248581-5ebc1c6c-b445-45b0-ab0f-3020e4672965.png)

### To Recreate Tables 
    Run main.py file

## What is done from Points to Archive
    All Points are archived as given:
   - [x] Your code should follow concept of OOPS
   - [x] Support for handling authentication requirements & token expiration of server
   - [x] Support for pagination to get all data
   - [x] Develop work around for rate limited server
   - [x] Crawled all API entries for all categories and stored it in a database

### Total Entries in Tables:
   - Api_metadata: 525 Entries
   - Api_category: 45 Entries

## What is not done from Points to Archive:
    N/A
    
## What would you improve if given more days
   If more days are given: - 
   - I would improve the efficiency of code 
   - Add a featured user can select data from a particular page of category and able to store in DB
   - Fix the JSON error which occurs rarely
    
