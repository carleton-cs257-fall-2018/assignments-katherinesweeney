Names : Owen Barnett, Justin Hahn, Kate Sweeney

	Our project is a two-player boxing game. The game involves two players
fighting each other on a 1D stage. Each fighter will be equipped with health 
(that does not regenerate), a health bar, energy (that does regenerate), an
energy bar, and several fighting moves. Each fighting move will take energy.
These moves include a punch, a kick, and a block. Each character can move left
and right on this stage and and depending how close a boxer is to the other
boxer attacks may hit or miss. In addition blocking consumes energy to not take
any damage. A boxer wins if he has decreased the opponent's health to
zero or he has more health when the timer runs out. 

MVC allows for the modular design of our game. It seperates out the tasks. 
The Boxer class is the model, the BoxerView class is the view, and the Controller
class is the controller. This allows the boxer class to focus only on the 
interactions between the two boxers. The view component also allows us to change 
between views efficently and effectively. MVC also allows the controller class to 
focus on controlling the game state. MVC also allows for ease of modification,
especially in our group of three. We can work on seperate pieces of the project
at the same time while avoiding merge conflicts.

Core Classes:
	- Boxer.java
	- BoxerView.java
	- Controller.java
	- Main.java

Credit to Assets: Street Fighter II on the SNES