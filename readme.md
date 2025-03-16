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
In this project I used environment variables to initialize a log level and a log destination, so you can specify where to save the logs and what level you want the logs to initialize at. I utilized this in the Interface class in the commands package, as part of using my command design pattern.
## Link:
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py

# Logging
In this project I used logging to log various things that happen and various errors I might encounter. I used logging.info to show things that happen, and logging.error to differentiate that something went wrong in my program and I want to document what and when it happened. I configured logging so that there would be a default place where it would be saved per the program, but you can also specify your own location or level to log at besides the default configurations. I utilized logging in all of my plugins to show where everything was happening. Obviously, running from the main function, you will use logging, but since it's not being imported in main.py I will not include that as a link.
## Link to where logging is initialized:
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py
## Link to where logging is tested:
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_log_and_env.py
## Links to where logging is used:
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/command.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/add/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/clear/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/delete/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/divide/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/exit/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/load/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/look/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/menu/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/multiply/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/save/__init__.py
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/subtract/__init__.py

# Design Patterns
##

# LBYL and EAFP
