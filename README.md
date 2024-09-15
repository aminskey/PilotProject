# Marine Life
## DDU themed pilot project
Currently, we are working on a project, 
that raises awareness about ocean life. 
Did you know that about 71% of the earth's surface is covered in water, 
and that we have only explored 5% of it? 

As we know, 
fish live in the ocean across the globe. 
With the perfect water temperature and pH value of water, 
fish and coral reefs and easily thrive. 

But that is unfortunately not the case. Due to global warming, <br> 
underwater life face new challenges: High temperature, rising water levels, <br>
occurrences of strong storms and strong acids in the ocean etc. But another underrated killer is Marine plastic. <br>

Marine plastic is responsible for degrading habitat and killing marine and coastal wildlife.
Deaths caused by suffocation, indigestion, starvation and entanglement etc. About 1,500 species in marine and terrestial environments are known to ingenst plastics (US EPA, 2024).

### How it affects us
Plastic debris is polluting the human food chain as well. Most of the fish that we eat have small microplastics in them, that we consume daily (or as often as we eat fish). In 2008 (yes a long time ago), Algalita researchers began finding that fish are ingesting plastic fragments and debris. Of the 672 fish caught during that voyage, 35% had ingested plastic pieces (Clean Water Action, 2024).

### The Assignment
You have been contacted by the United Nations, whom have hired you to develop a software product. Now the UN aren't experts in software development and have therefore contacted you to make a software product that advertises the UN and creates awareness about one or more of their 17 sustainability goals.
<br> <br>

... Further details are saved in a doc file ...

### Our Approach
The goal that we want to raise awareness about is Goal 14: Life below water.
Our main subgoals are goals 14.1 and 14.2, which are as follows:

1. By 2025, prevent and significantly reduce marine pollution of all kinds, in particular from land-based activities, including marine debris and nutrient pollution. <br><br>
2. By 2020, sustainably manage and protect marine and coastal ecosystems to avoid significant adverse impacts, including by strengthening their resilience, and take action for their restoration in order to achieve healthy and productive oceans.

We have created a prototype game, that has the sole purpose of making the player lose the game. 
As the player you have to steer a flock of fish away the incoming trash. 
The trash (for now) mainly consists of bottles and empty food cans.

The game takes place in a fish-tank like ocean. The fish's movements are limited to the box that confines them. Periodically (about 20-25 seconds) a wave of trash spawns in either sides of the tank. In any case if the fish eats the trash, it dies immediately.
After short intervals algae also spawn in the tank. If any fish eat from the algae, another fish is born and joins the flock, increasing the number of fish in the flock.  

For now the game is purely time based. The _"winner"_ is the one who survives for the longest. The rest is up to you to find out :D

## How to play
Checklist: 
````
1. Python version >= 3.10
2. pygame version >= 2.3.0
````
### Installation
#### Python
Linux:
````
sudo apt-get update
sudo apt-get install python
````

Mac and Windows:
````
You can easily find something on the web.
````

#### Pygame
First check if you have pip.
````
$> python<version> -m pip --version
pip 24.2 from C:\DIR\Python\Python312\site-packages\pip (python 3.12)
````

Well if you do then first update:
````
$> python<version> -m pip install --upgrade pip
````

Afterwards install:
````
$> python<version> -m pip install pygame
````

### Playing the game
Go to the main folder (the folder which has main.py).
Run the following:
````
$> python main.py
pygame 2.5.1 (SDL 2.28.2, Python 3.11.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
````

Use the mouse to navigate :D