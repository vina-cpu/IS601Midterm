# Midterm Calculator

# Project Install Instructions

## install 
1. clone
2. pip install -r requirements.txt

## testing
1. pytest
2. pytest --pylint
3. pytest --pylint --cov
4. pytest --num_records=10

# Description
This is my calculator project. It has 10 different functions, including add, subtract, multiply, and divide. It has some history functionality utilizing pandas such as storing history in a pandas dataframe, adding history, deleting a row of history, clearing the whole history, loading history from a .csv file, looking at the current history in the command line without saving (so you can see what you're doing when you delete or clear history),and saving history to a unique .csv files in a 'saves' folder. This project also has logging, so it will take your specific environment variables (in a .env file) and load logging so that it logs to a path you specify. I also made it compatible with some default variables so that if you don't specify any environment variables the logging will still work.

-note about build and testing, had to make it ignore log, environment, saving, and loading, because i didn't push those things (for obvious reasons), but they do pass on my local environment
-note about environment variables: i obviously did not publish this onto github but it does pass with the logs on my local environment

# Environment Variables

# Logging



## requirements
1. 