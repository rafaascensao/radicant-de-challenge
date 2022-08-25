# radicant-de-challenge
Solution for Radicant Data Engineering Challenge

## Prerequisites
* [poetry](https://python-poetry.org/). To install run `pip install curl -sSL https://install.python-poetry.org | python3 -`

## Structure
```
radicant-de-challenge
 ┣ .github
 ┃ ┗ workflows
 ┃ ┃ ┗ push.yml
 ┣ data
 ┃ ┗ ETFs.csv
 ┣ db
 ┃ ┗ radicant_challenge.db - The SQLite db that stores our Data
 ┣ infra - Not used but with more time would create the infra necessary to host
 ┃ ┣ main.tf
 ┃ ┗ versions.tf
 ┣ src - All the code for the API and models is defined here
 ┃ ┣ api
 ┃ ┃ ┣ __init__.py
 ┃ ┃ ┣ app.py
 ┃ ┃ ┗ utils.py
 ┃ ┣ models
 ┃ ┃ ┣ BaseModel.py
 ┃ ┃ ┣ ESGFund.py
 ┃ ┃ ┣ UserPreferences.py
 ┃ ┃ ┗ __init__.py
 ┃ ┗ __init__.py
 ┣ tests - Pytest tests
 ┃ ┣ __init__.py
 ┃ ┗ test_utils.py
 ┣ .gitignore
 ┣ README.md
 ┣ poetry.lock
 ┣ pyproject.toml
 ┣ radicant Data Engineering Case.pdf
 ┗ script_fill_table.py - Python script that cleans the data and stores it on the db
```
## Usage
This project only runs locally. To run the project run `poetry run start`. You might need to run `poetry install` before running the command.

If for some reason, you need to run the script that transforms the data and stores it on the db, just run `poetry run python script_fill_table`.

To run the tests, is as easy as running `poetry run pytest`

When the project is running, you can visit the Swagger Documentation on http://127.0.0.1:8000/docs

## Explanation on some decisions and future improvements
Must of the decisions were made based on the time I had for the challenge. With more time, I would probably change some things. Below, I will go over some things that with more time I would change or add.

### Database
The idea here was to run a PostgresSQL database, but that needs to run somewhere and setupping up everything (maybe in a Docker container) would require more time or even maybe hosting the DB on the cloud. Abstractedly, using PostgresSQL or SQLite is super similar since they are Relational Databases supported by most DBORM.

### Cloud
The initial idea was to host the API and the DB on AWS. This would be done via Terraform, and I would create a Docker container for the API and host it via ECS and the DB would be hosted on the AWS RDS. However I didn't have the time to setup everything, and decided to run everything locally instead.

### Field Verification
The fields, like fund_size and dominant_sector, that serve as query parameters, each one should be an enum. That way when the user queries the API with invalid field values an error would popup, instead of an empty response as it happens now.

### Documentation
With more time I would like to dive deeper on the FastAPI swagger documentation and improve a bit on the response part of the documentation.

### Data Provided
I created a script that cleans the DataFrame and stores the cleaned data as a table. In a production environment, this should hosted on some ETL tool, like Airflow, where we can monitor the process and raise alerts when the data is not as expected.

The cleaning that I did was based a bit on intuition since I did not have the time to look deeper into the file. Mainly there were the steps:
* From the `fund_sector_*` columns, retrieve the highest sector and its percentage;
* Remove all columns where the percentage of NaN is above 50%;
* Removed some columns that seemed redundant or just added little information.

In my view, for the challenge, the final result of the table didn't matter as much because the API would behave similarly with a different model for the table. 
