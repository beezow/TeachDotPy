# teach.py
Built for Hack Illinois 2019 by Charles Agriogianis, Andrew Fei, Maxwell Jong, Albert Li, Theodore Li, and Drew Zoghby.

## About teach.py
teach.py is developed primarily with educators in mind. 
teach.py parses through python code files and translates it into visual animations for data structures, variables, etc. 
This creates **meaningful** and **powerful** representations of code compilation.

## Implementation
teach.py is broken down into its processing and animation sections. 

### Processing:

Python files are read in as a String. The file is then parsed line by line, and custom logs are inserted into the script. These logs are then used to construct an animation.

### Animation:

The animation portion interprets json to create meaningful visualizations of data. teach.py then draws the data structure using the parsed json. The result is a stimulating animation for educators to use.
