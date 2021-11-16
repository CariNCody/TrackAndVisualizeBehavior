# TrackAndVisualizeBehavior
Three independent python scripts that can be combined to somewhat automatically track animal movement patterns, quantify paths (different variables), and visualize movement using heat maps.
Especially useful for low contrast environments.

## curiousfish.py
The Python script curiousfish.py calculates various variables in the context of an individual exploring a novel environment. Input data are a two-column table which contains the 2D swimming path given by consecutive integer coordinates X and Y of the surface of the test tank.

Version 2.0 (15.11.2021)

### The variables that are calculated by curiousfish.py are:
1) **swimming_distance** The distance includes repetitive swimming patterns as, for instance, up and down swimming along one of the walls of the test tank. This value increases with each new square on the grid the individual visits regardless of this site has been visited before or not.
2) **Total sites visited** How many of the sites defined by the customized grid have been visited by the focal individual? In contrast to the swimming distance, each site only counts once so that repetitive swimming patterns do not lead to a higher value.
3) **Percentage of total area visited** This value takes the Total sites visited parameter and expresses it as the percentage of the total area visited. This parameter is often used to quantify exploration behaviour in the open field test.
4) **Total sites rock, Percentage of area rock, Total sites sand, Percentage of area sand** These variables are calculated like 2) and 3) with the only difference that we are here interested in a specific area of the test tank. We divided the area into a rocky and a sandy area, mimicking two different habitats. These two areas can be defined in the beginning of the script (XRock, YRock)
8) **Habitat preference** Based on the four previous variables (4-7), habitat preference calculates which of the predefined areas was preferred by the focal individual. The range of the “Habitat preference” is between … and ...
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
