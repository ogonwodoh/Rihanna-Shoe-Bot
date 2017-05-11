On February 20th 1988 a legend, named Robyn Rihanna Fenty, was born. On March 9, 2017 the Fenty x Puma Spring 2017 Collection was released. The collection proved to be the revival of Puma Shoes as their popularity skyrocketed. This bot is in honor of Queen Rihanna and works to look up the price and available sizes of Puma shoes. Soon a feature will be added to purchase shoes.

How to use:
This is a program that looks up a model number of a Puma shoe and retrieves the current price of the shoe. The program name is main.py and it is written in Python 3. To run the program the user must supply a product number for a puma shoe via a required command line argument. When the user does this an instance of the class puma_shoe is created. The puma_shoe class then generates a URL for the product number if it exists, then scrapes the product web page for the price and available sizes and current price of the product. After getting this information the program interacts with the user in several ways:

There are also optional command line arguments:
The argument --c or --compare allows the user to enter multiple product numbers and create instances of the puma_shoe class for each product number.
The argument --h or --history allows for logging the price and sizes of the main product number entered 
The argument --t or --tester performs unit testing on the program by calling the tester function defined in main.py

The prompt: 
"Press h to see product history for this shoe.\nPress i to see info about this shoe.\nPress p for size analysis.\nPress c for comparisons.\nPress q to quit.\n" allows the user to interact with the program."

The user can press i at the prompt to see the information of the shoe that they entered as required command line argument.
The user can press h at the prompt to retrieve any logs of price and size of the main product number entered. This option only works if --h was entered as a command line argument.
The user can press p at the prompt to see if any of the product numbers received by the program are within the user's budget and available in the user's size. The user is prompted for his/her size and budget.
The user can press q to quit the program 

REPRODUCIBLE USE CASES:
Use any of the following product numbers: [190393, 190304, 355462, 365054, 365774]. You can also enter the product numbers of any known Puma shoe.

enter:
python3 main.py 190393  
-this will lead you the prompt:
o"Press h to see product history for this shoe.\nPress i to see info about this shoe.\nPress p for size analysis.\nPress c for comparisons.\nPress q to quit.\n" allows the user to interact with the program."
-If you press h, you will see the log displaying the info of the shoe with product number 190393.
-If you press c, you wont see anything because you didnt enter the -c command line option
-If you press p, it will prompt you for your size and budget, then compare the available sizes and price for the shoe and output the product number of the shoe if it is within your size and budget
enter:
python3 main.py 355462 --c 365774 190393 --t ---h

-If you press h, you will see the log displaying the info of the shoe with product number 355462.
-If you press c, you will see a tuple (product number, available sizes, and price) for all of the product numbers you entered in the command line
-If you press p, it will prompt you for your size and budget, then compare the available sizes and price for the shoes you entered in the command line and output the product number of the shoe if it is within your size and budget

