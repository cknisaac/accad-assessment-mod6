# IMPORTANT - READ BEFORE STARTING WEB APPLICATION!!!

-------------------------------------------------------------------------------------------------------------------------------

#### 

#### You need to initialize your AWS credentials using the export commands 

e.g. 

export AWS\_ACCESS\_KEY\_ID= (ur aws\_access\_key\_id here)

export AWS\_SECRET\_ACCESS\_KEY= (ur aws\_secret\_access\_key here)

export AWS\_SESSION\_TOKEN= (ur aws\_session token here)



You can find these by logging onto AWS, under AWS accounts -> click the account you want to use -> Access keys -> Option 1: Set environment variables







#### 

#### You need to create a DynamoDB database first



The web application works by first reading off an existing database. Without creating one, it has nothing to read off and will always return an error/an empty to-do list.











#### You need to ensure the name of your database is correct in the code
**TO PYTEST, please use the command:
pytest test/unit/todo_test.py -v


In app.py, under class TodoItem(Model):

the variables table\_name and region must be set correctly according to your database name and region respectively. The ones provided in the code are mine (Isaac's) :) 

