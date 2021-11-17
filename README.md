# TrackAndVisualizeBehavior
Three independent python scripts that can be combined to semi-automatically track animal movement patterns, quantify paths (different variables), and visualize movement using heat maps.
Especially useful for low contrast environments.


## FishyGrid.py by Cody Garcia
The Python script FishyGrid.py allows a user to quantify a critter's (or any moving subject's / creature's / animal's) path of movement. Using a transparent grid which can be overlayed with a video, a user can continuously click on the position of the critter. The grid is completely customizable using the variables below.

### The customizable variables of FishyGrid.py are:
1) **rows** The number of rows the grid has. This can be changed to any natural number. The more rows the grid has, the taller it becomes, since every field of the grid remains a square, no matter the number of rows or columns (2.).
2) **columns** The number of columns the grid has. This variable, just like rows (1.), can be changed to any natural number. The number of rows does not change the shape of the fields, since they always remain square. The size of the boxes is dependent on the number of columns in relation to the size (3.).
3) **size** The length of the grid. The size reflects the length of the grid in its number of turtle grid pixels. Sizes over 1000 are usually preferable. The size of each box is the size divided by the number of columns.
4) **roll** Tilts the grid to the left or the right. Negative values tilt the grid to the right, while positive values tilt the grid to the left. The roll value can be any real number. The value of roll reflects the degree at which the grid is tilted by.
5) **transparency** Defines the transparency / opacity of the grid. Can be any number between 0 and 1. 0 is completely transparent while 1 is completely opaque.

### Usage
When starting up the program the first thing one must do is enter the file name to append to or to create (into the shell). Text files are preferred, but CSV files work as well. Once one has entered the file name the program draws the specified grid. Once the grid has turned transparent, it is ready to be used. The grid can then be moved over a video or a feed. Once over the video, one can locate the position of the subject (critter, squirrel, fish, whatever you're tracking). Once the subject has been found it can be clicked on and a turtle should appear in the field where the cursor has clicked. The video can then be played, and the test subject can be clicked on again, once it has moved into the next field. Once the next field has been clicked on, the turtle should follow. As the turtle travels from box to box, its position is recorded in the Text or CSV file that was entered in the beginning. In addition, the turtle’s position is also output as a pair of coordinates in the shell.

### Operating the turtle's movements:
1) On a left click the turtle can only move one box left, right, up, down, or diagonally. The turtle then moves to the next box and turns, to show the user the previous box that was clicked on.
2) On right click the turtle can jump multiple boxes in a straight line, either forwards, backwards, upwards, downwards, or diagonally. On the way the turtle will record every box it passes through as it travels in the straight line to its new position.

### Input files:
The program itself is capable of creating files completely independently. When first opening the program, one has to enter a name of a file. The program then either appends to the file with the name that was given, or if there is no file with the given name, the program creates a new file with the name.

### Output files:
The program creates (or appends to) either .csv or .txt files. Text files are preferred since the program has been known to make mistakes when writing to open CSV files. The coordinates of the boxes that are clicked on are saved in 2 columns, x on the left and y on the right. The columns are separated by commas, so if the file is written as .txt, it can easily be renamed to .csv and be used as a CSV file.

### Error messages:
There are no expected error messages to be seen when using the program.


## PathVisualizer.py by Cody Garcia
The Python script PathVisualizer.py allows the user to create a heat map style visualization of a path that a critter (test subject, ostrich, amoeba, ackie, whatever) went through. The script was created to use files created by FishyGrid.py, but can be used on other files which use the same syntax / formatting.

### The customizable variables of PathVisualizer.py are:
1) **rows** The number of rows the grid has. This can be changed to any natural number. The more rows the grid has, the taller it becomes, since every field of the grid remains a square, no matter the number of rows or columns (2.).
2) **columns** The number of columns the grid has. This variable, just like rows (1.), can be changed to any natural number. The number of rows does not change the shape of the fields, since they always remain square. The size of the boxes is dependent on the number of columns in relation to the size (3.).
3) **size** The length of the grid. The size reflects the length of the grid in its number of turtle grid pixels. Sizes over 1000 are usually preferable. The size of each box is the size divided by the number of columns.
4) **Automatic** If the program should operate in "automatic" mode or not. This variable must be a Boolean, either True or False. If automatic mode is set to True, then the program will require the variable expression (5.).
5) **expression** The regular expression the program shall search for when in automatic mode. If unfamiliar with the concept of a regular expression and just want to iterate through all the files in a folder, just use the expression "*".

### Usage
1) If automatic mode is set to False, the program will start with a prompt (in the shell) requesting a file name. Once the name has been entered, the program searches for the file and creates an EPS file of the finished heat map. The EPS file is automatically saved into the same folder as the original file.
2) If automatic mode is set to True, the program will automatically iterate through all files that match the regular expression. For each file it will create an EPS file and save it to a folder in the same location the program is operating in.

### Input files:
The program was designed to be able to take files directly from the FishyGrid.py program. The files shall have 2 comma separated columns. The column on the left shall contain the X coordinates, while the column on the right shall contain the Y coordinates. The first line of the input file is ignored since the program expects there to be a header there. The file type can be either Text or CSV.

### Output files:
The program outputs EPS files of the heat maps. The EPS files have the same name as the input files with the ending .eps added on.

### Error messages:
If the program failes to create a folder, the folder could have been already been created, in which case the program would save the heat maps to the already existing folder for the heat maps. If there is no already existing folder for the heat maps, and the program failes to create the folder, the program does not have the proper permissions to function properly.




## curiousfish.py by Carolin Sommer-Trembo
The Python script curiousfish.py calculates various variables in the context of an individual exploring a novel environment. Input data are a two-column table which contains the 2D swimming path given by consecutive integer coordinates X and Y of the surface of the test tank.

Version 2.0 (15.11.2021)

### The variables that are calculated by curiousfish.py are:
1) **swimming_distance** The distance includes repetitive swimming patterns as, for instance, up and down swimming along one of the walls of the test tank. This value increases with each new square on the grid the individual visits regardless of this site has been visited before or not.
2) **Total sites visited** How many of the sites defined by the customized grid have been visited by the focal individual? In contrast to the swimming distance, each site only counts once so that repetitive swimming patterns do not lead to a higher value.
3) **Percentage of total area visited** This value takes the Total sites visited parameter and expresses it as the percentage of the total area visited. This parameter is often used to quantify exploration behaviour in the open field test.
4) **Total sites rock, Percentage of area rock, Total sites sand, Percentage of area sand** These variables are calculated like 2) and 3) with the only difference that we are here interested in a specific area of the test tank. We divided the area into a rocky and a sandy area, mimicking two different habitats. These two areas can be defined in the beginning of the script (XRock, YRock)
8) **Habitat preference** Based on the four previous variables (4.), habitat preference calculates which of the predefined areas was preferred by the focal individual. The range of the “Habitat preference” is between … and ...
9) **Habitat preference normed** Since we wanted to compare our habitat preferences with habitat scores of another study, we normalized the score in order to force the scores to lie between -1 and 1.
10) **Border sites** This variable calculates how many of the border sites of the test tanks (=all sites touching the walls of the test tank) were explored.
11) **Percentage border sites** This variable is often used to quantify thigmotaxis, which is a measurement of anxiety in fish and other animals. The variable calculates the percentage of border sites visited compared to non-border sites of the tank. Similarly like in 3), sites are only counted once so that repetitive swimming behaviour do not bias this value.
12) **Percentage border sites normed** This variable considers that in our experimental design, there are more non-border sites than border sites, and corrects for this underlying bias. 

### Input files:  

csv-files with two columns (left column: X coordinates, right column: Y coordinates). For example, if our focus individual started at position 6/5 on our grid, this is the first row in the csv file. The next position the individual takes will be the second row etc. Per default, each csv file has a simple header: X for the first and Y for the second column.

Once, the swimming path of each individual is identified by one such csv file, they should be organized in a folder together with the curiousfish.py script. The program can be run by open the terminal, navigate to the folder including all the files and the program by the following command:
user> python3.7 curiousfish.py                                                                                          

By default the files should be named as id*.cvs where “*” stands for any string in the file name such as numbers of the consecutive files containing the swimming paths. The filename patterns can be redefined in the script.
                        
The package glob is used to handle pathname pattern expansions for file names.                       

### Output files:  

csv table containing all the 12 variables described above.

### Error messages:

Only python errors will be shown (missing file name, wrong format of the data etc.). There is no specific error output defined.


### History:
Initially, this script was written together with the scripts FishyGrid and PathVisualizer (by Cody Garcia) to track the swimming behaviour of rather small fish in a low-contrast environment. A common prerequisite under which many tracking programs work is a high contrast between the individual to be tracked and its environment. However, in some contexts a low-contrast environment is more biologically meaningful and, in these cases, our half-automated package can help to bridge this gap.
