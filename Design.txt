Danny Godwin
12/07/20
CS5001

CS5001 Final Project - Matching Game in Python
Documentation 

	Design

    - First step was to import the turtle, time and random modules
    - Created the board using a background image with the 'quit', 'status' and 'leader' already displayed from a screenshot of the board I originally created for saving time during the 'loading' portion of the game. 
    - Created turtles 'Status', 'Match', 'Leader' to display 0 moves/matches and the leaderboard for the top 8 players in order.
    - Opened Leaderboard txt file containing all players who have played before with their score first and then their name. For each line of the txt file with open, the scores are appended to a list titled 'score' and then sorted from least to greatest.
    - The list is limited to the top 8 players using list slicing and then using leaders turtle, the list is written on screen.
    - For the main function, I created a global name variable and assigned to the the screen text box that appears at the beginning of the game to collect the players name. 
    - Another screen text box to setup # of cards. A while loop to make sure that player inputs are 8,10,12 or an invalid entry message pops to prompt user to enter a valid entry.
    - # of cards from text box above is converted into an integer which is placed as a parameter in a new function called 'card_distro' to distribute the cards.
    - From a list of cards in the 'card_distro' function, the list is shuffled using the random module and depending on the functions only parameter 'number' which is 8,10,12, the appropriate number of cards is created using the 'Card' class and placed in the correct coordinates pre mapped out. 
    - For the 'Card' Class, the initializer has the parameters self, image and the coordinates. It creates 2 turtles, the back face of the card which is the same for every card and the front face being the image parameter which is unique. 
    - 'Card' class has following methods:
		
		.x_axis - returns attribute x coordinate
		.y_axis - returns attribute y coordinate
		.flip - hides attribute back of card, shows front
		.same - returns name of the front face gif image
		.remove - hides attribute back of card and front and clears corresponding turtles
		.win - returns False if both attributes back face and front face of card are hidden. 
		.is_visible - returns visibility of back face card
		.reset - shows attribute back face card and hides front face card

    - Back to the main function, guesses and matches variables are created and set to 0.
    - Screen on click function starts the game.
    - If the click is around the 'quit' box, game ends
    - If the click is within the coordinates of the cards, the coordinates are collected to see if it matches any of the card coordinates stored as a attributes for each card. A visibility function is created to store whether its the first or second card. If false, its the first card
    - The player can click again but this time, the visibility function is true meaning this is to flip the second card. If the click coordinates match that of any cards created, that card is flipped. A time sleep period of 1 second is given for the user to remember the location of the cards. 
    - During this period, the 2 cards return the files names of the gif images using the .same method and if they match, the .remove method is invoked from the card classes and the 2 card are hidden. The matches variable is now added 1 and is displayed in the status area.
    - If the cards do not the match, the .reset method is invoked for both cards flipping back the cards to their original state. The guesses variable is now added 1 and displayed in the status area.
    - Once the player matches all the cards, the .win function is invoked on very single card. If the front face and back face of every card is hidden, the player wins and the turtle image 'You won!'  is displayed. 
    - Before quitting the turtle and ending the game, the leaderboard file is opened and the name and total guesses of the player is written. 

	Testing

	The way I approached testing was sticking fast to the method of 'failing fast' that Professor Bagley mentioned during lectures. I tested the game iteratively throughout the process of creating of the game. From the start, making sure only 8,10,12 could be entered and not any other number. Using this fail fast method, I broke down the game card logic into mini goals and made sure I reached those mini goals before moving. Or else, I would take a break from it if I was stuck to work on another aspect of the game. Since creating turtles and displaying them took time, I screenshot the board and displayed that. I also, quickly printed results I wanted to see to the shell and test if they worked or not instead of immediately displaying them on the screen such as the leaderboard and status area. To test the leaderboard, I put dummy date in the text file including various scores and names. In my code using this dummy data, I tested whether my list sorting method worked and made sure the screen only displayed the top 8 scores. As for the major portion of the design being the card behavior, I approached this by making sure my class card worked with 1 card and then repeating this for 8,10,12 cards. I also printed simple booleans of the status of the cards to avoid having to boot up the game each time. I tested the game against every scenario I could think of including attempting to enter 0 or 9 cards, playing the game with 8 cards, then 10, then 12, using the quit button and making sure nothing was written to the leaderboard txt file and attempting to click on the same card twice.



