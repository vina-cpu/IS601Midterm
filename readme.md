# Midterm Calculator  
  
# Project Install Instructions  
  
## install 
1. clone
2. pip install -r requirements.txt  
  
## testing
1. pytest
2. pytest --pylint
3. pytest --pylint --cov  
  
# Description  
This is my calculator project. It has 10 different functions, including add, subtract, multiply, and divide. It has some history functionality utilizing pandas such as storing history in a pandas dataframe, adding history, deleting a row of history, clearing the whole history, loading history from a .csv file, looking at the current history in the command line without saving (so you can see what you're doing when you delete or clear history),and saving history to a unique .csv files in a 'saves' folder. This project also has logging, so it will take your specific environment variables (in a .env file) and load logging so that it logs to a path you specify. I also made it compatible with some default variables so that if you don't specify any environment variables the logging will still work.  

-note with cov: my overall coverage with the tests i did not put on github to run in actions is 95%, even though it's showing up as 92% in the build    
-note about build and testing, had to make it ignore log, environment, saving, and loading, because i didn't push those things (for obvious reasons), but they do pass on my local environment  
-note about environment variables: i obviously did not publish this onto github but it does pass with the variables on my local environment  
-note: most of my loss of coverage is due to the exception cases for generic cases not being covered in the tests; i tested everything i could and planned for, but i didn't find it worthwhile to test for a generic error, especially when that exact code works for some errors (such as in load_history() and the test for it); felt like it would crowd my test cases    
# REPL  
I used Read, Evaluate, Print, Loop (REPL) in the Interface class, where I continuously wait for user input in a loop, to provide the user to do various actions using all of my plugins via the Command class.  
Link to how I use REPL here:  
https://github.com/vina-cpu/IS601Midterm/tree/main/commands  
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/main.py  
# Environment Variables  
In this project I used environment variables to initialize a log level and a log destination, so you can specify where to save the logs and what level you want the logs to initialize at. I utilized this in the Interface class in the commands package, as part of using my command design pattern.  
Link for environment variables usage:  
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py  
# Logging  
In this project I used logging to log various things that happen and various errors I might encounter. I used logging.info to show things that happen, and logging.error to differentiate that something went wrong in my program and I want to document what and when it happened. I configured logging so that there would be a default place where it would be saved per the program, but you can also specify your own location or level to log at besides the default configurations. I utilized logging in all of my plugins to show where everything was happening. Obviously, running from the main function, you will use logging, but since it's not being imported in main.py I will not include that as a link.  
Link to where logging is initialized:  
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py  
Link to where logging is tested:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_log_and_env.py  
Links to where logging is used:    
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
# Pandas  
I used the pandas DataFrames in the History class, to streamline history management. With pandas, I can save data that is formatted to a .csv file, and I can also load data that is formatted to a .csv file. This means that I can load previous history, and pick up where I left off. I can also delete specific rows, clear all the history, and look at all of my formatted history through the command line without saving, all due to pandas.  
Link to History class:  
https://github.com/vina-cpu/IS601Midterm/blob/main/history/__init__.py  
Link to History testing:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_history.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_save_and_load.py  
# Design Patterns  
## Facade  
I utilized the facade pattern in the History class and the plugins. This allowed me to shield the user from complex things that I was doing behind the scenes, and simplify them with simple commands like "add" or "save". This lets me do all of the heavy lifting on the backend, while from the user's perspective, the program is really simple.  
Link to History class:  
https://github.com/vina-cpu/IS601Midterm/blob/main/history/__init__.py  
Link to all the plugins:  
https://github.com/vina-cpu/IS601Midterm/tree/main/plugins  
Link to Command and Interface, where I let the user interact with the plugins:  
https://github.com/vina-cpu/IS601Midterm/tree/main/commands  
Links to testing:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_command.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_calculator.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_history.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_save_and_load.py  
## Command  
I utilized the command pattern in the Command and Interface. This allows me to make plugins and dynamically add them to the list of "requests" that the Command and Interface classes are able to handle.  
Link to commands folder with Command and Interface classes:  
https://github.com/vina-cpu/IS601Midterm/tree/main/commands  
Links for testing:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_command.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_calculator.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_history.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_save_and_load.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_log_and_env.py  
## Factory  
I utilized the factory pattern in the calculation and calculator classes. This makes it easy for me to duplicate operations by making a new instance each time I want to perform a calculation (Calculation class), or perform a calculation and also save it to memory (Calculator class, used in REPL command-line interface)  
Link to Calculator class:  
https://github.com/vina-cpu/IS601Midterm/blob/main/calculator/__init__.py  
Link to Calculation class:  
https://github.com/vina-cpu/IS601Midterm/blob/main/calculator/calculation.py  
Link to testing:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_calculation.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_calculator.py   
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_calculator.py  
## Singleton  
I utilized the singleton pattern in the History class. I only want one history, and I don't want another instance. This would get confusing if I had multiple instances of histories because I wouldn't know which history I am appending to or loading to, and wouldn't know what I am getting when I am saving. These problems were mitigated by making the History class a singleton, because I don't have to worry which History instance I am saving to, as there is only one.  
Link to History class:  
https://github.com/vina-cpu/IS601Midterm/blob/main/history/__init__.py  
Link to History testing:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_history.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_save_and_load.py  
## Strategy  
I used the strategy pattern by implementing plugins. These plugins all have their own classes, but perform similar, yet different operations. I have a few for calculator operations, and those are very similar, and then I have a few for manipulating data in the History class. These kind of act like my two groups inside plugins that are similar to each other, and are similar strategies.  
Link to plugins:  
https://github.com/vina-cpu/IS601Midterm/tree/main/plugins  
Link to plugins testing:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_calculator.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_history.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_save_and_load.py  
# LBYL and EAFP  
I used "Look Before You Leap" (LBYL) and "Easier to Ask Forgiveness than Permission" (EAFP) in different situations. I used LYBL where I had "if" statements, because I knew that I would be going through that "exception" case most of the time. I used this in my implementation of getting my environment variables, because I really only had two cases that I was looking for, so there really weren't exceptions, because the two scenarios were each likely to happen at the same time. I also used it in my testing of calculator, because I wanted to separate when I tested for division by non-zero numbers and division by zero, and using an "if" statement in this case made more sense, because I always want to check for that case that b != 0, and want to do nothing otherwise, so it made no sense to try to do that with an "except" case as in EAFP.  
I used EAFP when I knew that I would be using the default case most of the time, so where "try" happens it would most likely happen. I used this in all of my plugins, where I want those exceptions to happen on a rare basis, and the try cases would probably be used the most. Here it is easier to just try the thing I am trying to do, and handle exceptions as they come, because they don't come often.  
Basically, I used LBYL when I would need to check for things all of the time, and used EAFP when I would rarely touch those exception cases.  
Links to where I used LBYL:  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_calculation.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_calculator.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_operation.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/calculator/operation.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/command.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/main.py  
Links to where I used EAFP:  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/add/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/clear/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/delete/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/divide/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/load/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/look/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/menu/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/multiply/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/save/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/plugins/subtract/__init__.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/commands/command.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_calculator.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_interface_history.py  
https://github.com/vina-cpu/IS601Midterm/blob/main/tests/test_save_and_load.py  
# Video  
Link:  

