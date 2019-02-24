# teach.py
A new open source project built for the Open Source Challenge of HackIllinois 2019 by Charles Agriogianis, Andrew Fei, Maxwell Jong, Albert Li, Theodore Li, and Drew Zoghby.

## About teach.py
For many beginners, visualizing code is often difficult and intimidating. Computer science concepts such as lists, loops, and queues can be very confusing. *teach.py* is developed primarily with educators in mind to better demonstrate these fundamental ideas. 
*teach.py* parses Python code and translates it into visual representations, creating **meaningful** and **powerful** images and animations.

## Implementation
We created *teach.py* in two parts: code analysis and animation generation. Native Python files are first parsed line by line, and custom logs are inserted into the script. Running the edited script produces a custon JSON populated with important events and information about the code. We then use Processing to create meaningful visualizations of the JSON data. Our program then visualizes the relevant data structures and modifications, resulting in an enriching animation and powerful tool for educators.
