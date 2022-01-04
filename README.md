# PC-Builder
This was a final project made for the class python concepts and methodology I, taken in fall 2020. The assignnment was as follows:

The final project for the class is principally a gui driven webscrape. Here're the requirements:

Scrape a website (or websites) or use an API to obtain information from a remote service.
All of the user interaction must be in the gui.
Information scraped from the web must be processed or parsed.
There must be at least one of each:
class defined and utilized in the code
loop
a file read or write
The script must be split across several files.
Docstrings must be utilized.
Code must adhere to PEP 8.
Sample Project:
A gui that allows you to generate a quote for supplying a local school with a basic 3d printing setup. It has the following parts:

Allow the user to select a 3d printer from one of several models. (Dropdown list?) Scrape the current price from the supplier.
Allow the user to select a material for filament (you don't need to check that the printer can support it), scrape the prices for several colors and average them.
Allow the user to enter a number of rolls of filament.
Incorporate all of the scraped and entered information into a shopping cart class. Run a method of the shopping cart class to generate a quote. Sales tax? Shipping?
Display the quote on the Gui with a save button.
Quote must be dated.
User changes to the above should change the quote.
The save button should write the quote to a file, it can be a simple text document, but nice formatting is nice. 

Project explanation:
Firstly, the user must enter their total budget for the PC. The program will then divide it up into allocations for each part. I set defaults for each part based on experience and
testing, but the user has the ability to motify how much each part will be allocated. Once the user runs the program, it will go to Newegg.com and searches on the webpage
that is passed to the method. It will search for the most expensive part that it can buy with the allocated budget of the part, and saves that to display to the GUI. 
Once the GUI has run, the user has the option to save the results to a file, where they can access it later. 
