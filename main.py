
# Function `print` prints the values to a stream, or to sys.stdout by default.
print("Hello, World");

worldStr: str = "World";

print("Hello, " + worldStr);


# By using %s, we can do string formating and inject a variable
# It is cleaner and more readable than using string concatenation
print("Hello, %s" % worldStr);

# The line below would cause an error
# %i expects a numerical value to be supplied
# print("Hello, %i" % worldStr);


# This script can be run simply by typing
# `python3 main.py` in your terminal
# Note that you will need to have python3 installed on your system

# To enable type annotation check, you need to install `mypy`.