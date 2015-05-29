Windows PC Starter Kit
Martin O'Hanlon

From the book: "Adventures in Minecraft"
 written by David Whale and Martin O'Hanlon, Wiley, 2014
 http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

-------------------------------

Description
------------------------------- 
This starter kit contains a pre-configured Canarymod server and a folder called "MyAdventures" which contains all the Python libraries required to complete all the chapters in "Adventure in Minecraft".

It is highly recommended that you use the Starter Kit as is and follow the instructions in Adventure 1 - "Hello Minecraft World" to setup your computer.  

The structure of the StarterKit zip file is as follows:
AdventuresInMinecraft
 - Canarymod : contains the pre-configured canarymod server and always creative and raspberry juice plugins
 - MyAdventures : folders to save the minecraft programs too
   - mcpi : python api library distributed with Minecraft: Pi Edition
   - anyio : python library for controlling hardware
 - StartCanary.bat : a batch file used to start the canary server
 - findPort.py : a python program used in adventure 5 to find the com port a connected arduino uses
-------------------------------


StarterKit Creation Guide
-------------------------------
If required the information below can be used as a guide to create your own StarterKit from scratch.  It is written as guide, not as a precise series of instructions.  There is no guarantee that they are accurate and are provided as is.

You can use either Bukkit or Canarymod for the minecraft server.  Follow the instructions to Download and run either Bukkit or Canarymod not both!

Create folders
----------------------
Create a folder "AdventuresInMinecraft"

Create a folder "AdventuresInMinecraft\Bukkit"
             or "AdvenutresInMinecraft\Canarymod"
(depending on whether you want to use Bukkit or Canarymod)

Create a folder "AdventuresInMinecraft\MyAdventures"

Download and run Bukkit
---------------------
Download Bukkit from dl.bukkit.com and put it in "AdventuresInMinecraft\Bukkit", the file will be named  craftbukkit-#.#.#-R#.0.jar   where the # s are the current version number; make a note of the version number, you will need this later.

Rename the downloaded .jar file from  craftbukkit-#.#.#-R#.#.jar  to  craftbukkit.jar .

Open Notepad and insert the following text:

java -Xms1024M -Xmx1024M -jar craftbukkit.jar
PAUSE

Save the file in notepad to the  Bukkit  folder as  start.bat .

The start.bat file is a windows batch program which will startup the Bukkit server when it is run.

Double-click the start.bat file to run it and startup Bukkit.

Because of issues with java not being consistently being available to run from the command line, Launch4J (launch4j.sourceforge.net) was used to create an exe called start.exe which launches bukkit.

When you first start Bukkit it will take a little time to run as it sets up the server and creates a new Minecraft world, when it s finished you will see the message  Done  in Bukkit s command window.

When you want to start your Minecraft Bukkit server in the future you can double click on the start.bat file.

To stop Bukkit, enter the word  stop  into the command window and press Enter.

 - Configure Bukkit
 ----------------------
Open Notepad, click File, Open and goto the Bukkit folder on the Desktop, change the  Text Documents (*.txt)  to  All Files (*.*)  and open  server.properties .

By changing the  server.properties  files you can change how Bukkit is setup.
Change:
 -  gamemode=0  to  gamemode=1  to change the server from survival mode to creative.
 -  force-gamemode=false  to  force-gamemode=true  to make all players play in creative mode.
 -  spawn-monsters=true  to  spawn-monsters=false  so monsters mobs won t appear in the game.
 -  allow-flight=false  to  allow-flight=true  so you can fly in Minecraft.
 - "online-mode=true  to  online-mode=false  so you don t need to be connected to the internet to use Bukkit

 - Create StartBukkit.bat
 ----------------------
Open notepad and add the following text:

ECHO OFF
ECHO "Adventures In Minecraft"
ECHO "Bukkit Minecraft Server Version is #.#.#"
ECHO "  Note - make sure Minecraft is using version #.#.#"
pause
cd Bukkit
start.bat
pause
ECHO ON

Replace #.#.# with the version number of Bukkit you downloaded.

Save the folder as StartBukkit.bat to the MyAdventures folder

 - Install RaspberryJuice
 ----------------------
RaspberryJuice is a plugin for Bukkit which will allow you to write programs which will change the Minecraft world as you are playing, just like the API which comes with Minecraft: Pi Edition on the Raspberry Pi.

Goto dev.bukkit.org/bukkit-plugins/raspberryjuice/ and download the latest version of the raspberry juice plugin, download the raspberryjuice-#.#.jar file.  

Copy the raspberryjuice-#-#.jar plugin to the plugins folder in the Bukkit folder.

Download and run Canarymod
---------------------
Download Canarymod from http://canarymod.net/releases and put it in "AdventuresInMinecraft\Canarymod", the file will be named CanaryMod-#.#.#-#.#.#.jar   where the # s are the current version number; make a note of the version number, you will need this later.

Rename the downloaded .jar file from CanaryMod-#.#.#-#.#.#.jar  to  CanaryMod.jar .

Open Notepad and insert the following text:

java -Xms1024M -Xmx1024M -jar CanaryMod.jar
PAUSE

Save the file in notepad to the  CanaryMod  folder as  start.bat .

The start.bat file is a windows batch program which will startup the Canarymod server when it is run.

Double-click the start.bat file to run it and startup Canarymod.

The first time you start you will be asked to agree to the EULA.

Open the eula.txt file in the Canarymod folder:
Change  eula=false  to  eula=true
Save the file and run the start.bat file again.

When you want to start your Minecraft Canarymod server in the future you can double click on the start.bat file.

To stop Canarymod, enter the word  stop  into the command window and press Enter.

 - Configure Canarymod
 ----------------------
Open Notepad, click File, Open and goto the Canarymod folder on the Desktop, change the  Text Documents (*.txt)  to  All Files (*.*), open the following files and make the changes below:

Open config\server.cfg
Change:
 -  online-mode=true  to  online-mode=false  so you dont need to be connected to the internet to use Canarymod
 -  player-idle-timeout=1  to  player-idle-timeout=0  so you players arent disconnected when idle for 1 minute


Open config\worlds\default\default_NORMAL.cfg
Change:
 -  gamemode=0  to  gamemode=1  to change the server from survival to creative
 -  spawn-protection=16  to  spawn-protection=0  so the spawn area can be built on
 -  spawn-villagers=true  to  spawn-villagers=false  to turn off mobs
 -  spawn-golems=true  to  spawn-golems=false
 -  spawn-animals=true  to  spawn-animals=false
 -  spawn-monsters=true  to  spawn-monsters=false

 - Give players permissions
 ----------------------
By default no players have permissions in Canarymod.  To give yourself admin permissions on the server type:

playermod group add playersname admins

e.g.  playermod group add martinohanlon admins

in the Canarymod command window.

 - Create StartCanaryMod.bat
 ----------------------
Open notepad and add the following text:

ECHO OFF
ECHO "Adventures In Minecraft"
ECHO "Canarymod Minecraft Server Version is #.#.#"
ECHO "  Note - make sure Minecraft is using version #.#.#"
pause
cd Canarymod
start.bat
pause
ECHO ON

Replace #.#.# with the version number of Canarymod you downloaded.

Save the folder as StartCanarymod.bat to the MyAdventures folder

 - Install RaspberryJuice
 ----------------------
RaspberryJuice is a plugin for Canarymod which will allow you to write programs which will change the Minecraft world as you are playing, just like the API which comes with Minecraft: Pi Edition on the Raspberry Pi.

Goto https://github.com/martinohanlon/canaryraspberryjuice and download the raspberry juice plugin and source code.

From the jars folder copy the raspberryjuice-#-#.jar plugin to the plugins folder in the Canarymod folder.


Setup MyAdventures folder
----------------------
Download mcpi(*) from github https://github.com/martinohanlon/mcpi
   * - the mcpi folder contains the python library supplied by mojang with Minecraft: Pi Edition and the minecraftstuff library (github.com/martinohanlon/minecraft-stuff) by Martin O'Hanlon 

Copy the mcpi folder to AdventuresInMinecraft/MyAdventures

Download anyio from github https://github.com/whaleygeek/anyio

Copy the anyio folder to AdventuresInMinecraft/MyAdventures

Copy the findPort.py file to AdventuresInMinecraft/MyAdventures
-------------------------------