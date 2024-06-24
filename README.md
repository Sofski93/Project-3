# Battleships - Project 3

Battleships is a Python terminal application which runs on the Code Institute mock terminal on Heroku.

The game is about finding the computer`s ships before they finds them.

<img src="https://github.com/Sofski93/Project-3/blob/main/4.png">

Live link to the application is here https://p3s-c229fe40048e.herokuapp.com/

## How to play

Battleships is based on the classic pen and paper game.
In this version the game stars directly when entering the page.
The player can not see the ships.
The player and the computer then take it in turns to make quesses and try to sink each other´s battleships.
The winner is the player who sinks all of their opponent´s battleships first.

## Features 

<img src="https://github.com/Sofski93/Project-3/blob/main/1.png">
+ You must enter number and row
+ You cannot enter the same number and row twice
+ It says how many attempts you have left

<img src="https://github.com/Sofski93/Project-3/blob/main/2.png">
<img src="https://github.com/Sofski93/Project-3/blob/main/3.png">
  
## Testing

I have tested this game in safari, edge and chrome.
Have also tested in my iphone


## Bugs, Issues and Errors

No bugs


## Deployment

The following were the steps undertaken to deploy the project to Heroku:
+ In the gitpod terminal, run 'pip3 freeze > requirements.txt' to install dependancies such as gspread and google auth into the Heroku platform.
+ After login to Heroku account, create a new app.
+ Navigate to settings tab, and go to Reveal Config Vars button
+ Add new Config vars  and enter value of 8000 for the PORT key.
+ Click "Add Buildpack" and add Python and Node.js in that order
+ Navigate to Deploy tab, choose Github and confirm connection to github account
+ Click Deploy Branch, and application is now deployed.


## Credits

+ Code Institute - Gitpod template provided for development
+ Heroku - Hosting platform for deployment      
