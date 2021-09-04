# Postman Web Scraping Project 
### Project - Get metadata from API and store in a database. 
## Problem statement

On the landing page of the above repo, you can see some list of categories for e.g. Animals, Art & Design, Business etc.
In the next section you can find some API details for each one of the categories for e.g. under Animals section we have 
API:  Cat Facts, Link: https://alexwohlbruck.github.io/cat-facts/
Description: Daily cat facts, Auth: No, HTTPS: Yes, CORS: No
We need to crawl the above list of all APIs and store it in a database. You can find the public API here with Postman documentation.
Do not use any other APIs or scraping method to get the data. 
Note: You just need to fetch and store a list of all API in the database and NOT data from each API.


#### Given  -  POSTMAN API 
## Step to run a code:
#### Step 1: Clone/download files              
#### Step 2: Enter into Project folder        
#### Step 3: Execute the following cmd: 
    $ Python main.py
### Output
Two output file generated
- api_database.db api_database content two tables Api_metadata and Api_category 
- csv_file as Data, Data contains a Api_metadata 
## Details of all the tables and their schema:
#### There is Two tables in the database: 
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
Command to recreate main.py file 
    

## What is done from Points to Archive
###### All Points are archived as given:
- [x] Your code should follow concept of OOPS
- [x] Support for handling authentication requirements & token expiration of server
- [x] Support for pagination to get all data
- [x] Develop work around for rate limited server
- [x] Crawled all API entries for all categories and stored it in a database

### Total Entries in Tables:
   - Api_metadata: 525 Entries
   - Api_category: 45 Entries
   
## What would you improve if given more days
   If more days are given: - 
   - I would improve the efficiency of code 
   - Add a featured user can select data from a particular page of category and able to store in DB
   - Fix the JSON error which occurs rarely
   - Implement on docker  
    
