Welcome to EasyEdits!

For this help page but better formatting + images:
https://docs.google.com/document/d/1KBCyDokTxtbWW3JRwVdAvVOeqLpRNL3zg-qB0INId6w/edit?usp=sharing

EasyEdits Help Doc

Basic Layout Rundown:

Main File Viewer: Displays the contents of the “PRESETS_HERE” Folder
Mini File Viewer: Displays the selection of the Main File Viewer
Outputs: Displays the data of the top selected preset in the Mini File Viewer
Prefix/Name Preview: Previews what the name + prefix will look like, updates on click
Apply Output Changes: Applies all checked outputs to presets selected in the Mini File Viewer
Preferences: Opens a new preference window where you can customize settings
Loading Bar: Loads during functions, you probably won’t ever see it move unless something goes wrong
Exit: Close the program, don’t use the X, use the Exit button
Setup:

The 3 things you have to worry about is the “PRESETS_HERE” folder, the “backup” folder, and the ‘EasyEdits’ application.

Steps:
Make a new folder in your Vital presets folder of all the presets you want to change.
Copy, not cut, COPY the presets in that new folder into the “PRESETS_HERE” folder in EasyEdits.
Also copy the presets into the “backup” folder in case something goes wrong, especially since this has still only been tested by me.
Run the ‘EasyEdits’ application, it should take several seconds depending on how many presets you are altering.
Make your modifications.
Open a few of the presets to check and make sure everything has worked.
Copy all the presets
Navigate back to your Vital presets folder and delete the contents of the new folder you made in their earlier.
Past in your edited presets and your good!


Navigating the UI:


Main UI:


File viewers:

There are a few things to unpack here so let's get started!

The main, and larger, file viewer displays all of the data of your presets in “PRESETS_HERE”. You can change the size of the columns by dragging on the dividers. The first column “File” contains the file names, you can drag the dividers to resize and view them. 

For selecting:
One: Click
Multiple Connected: Shift + Click
Multiple Divided: Ctrl + Click

The “Select by Value” area is how you can mass select similar presets. The “Value here” box is where you put in what you're looking for, and “Select by Value” is where you’re looking for it.

The Mini Viewer is where your selected presets from the bigger viewer go. It condenses your selection into only what you have selected and makes it easier to manage large file batches.

Below the Mini Viewer is your selection options for it.
Eye: Opens Vital with the focused preset, aka whichever one's data is in the outputs
All: Selected everything
Invert: Inverts selection
Below/Above: Selects all below/above focused preset



Output Boxes:

There is even more here to unpack, so let’s begin!

The Prefix, Name, Author, Style, and Description Boxes are used to show the data of the focused preset. You can edit them and then press the check directly across from it to make those edits go into effect when “APPLY TO SELECTED” is pressed.

APPLY TO SELECTED is the button you press when you’re ready. It will apply the changes you made to every preset selected in the Mini Viewer. You can see how this will look by using the Prefix/Name previewer.

Prefix/Name viewer is where you can see how the new name will look and change the focused preset, with the arrows. When you have changed the data in either the Prefix or Name boxes and activated their respective checkboxes, clicking any empty space will update the box letting you preview how the prefix and name boxes will combine.

The Break Box is where you can enter the character that is used to divide the prefix from the name. If I had the preset name ‘LD_Cool Lead’, I would put ‘_’ in break to signal that ‘_’ is where the prefix ends. If I want to use Whitespace, you would enter in ‘%’ which is the default and can be changed in the preferences window.

Replace? Is where you can decide how the new prefix is appended on to the Name box. Checking it will replace the old prefix with the new one, but leaving it unchecked will just append it to the old prefix.

The Checkboxes are how the program knows what to change. By checking a box, you are saying that you want the value currently in there to be given to all the selected presets in the Mini Viewer. 

The prefix/name/replace checkboxes can get really confusing so I suggest you just experiment with getting the results you want. Ex: ‘I want to change the name but append my new prefix to the original prefix’ would be a check on Name, Prefix, but Replace is unchecked. Another thing to look out for is the ‘replace duplicate prefixes’ checkbox in the preferences window. Right now it’s very buggy and can cause unexpected results, so I wouldn’t mess with it. It will be fixed in the Final release

The Save/Edit Icons are how you save your custom prefixes/styles. The save icon will save whatever is in the box next to it to your customs. The edit icon will pull up a window where you can remove, add, and save all of your custom styles and prefixes.

That’s pretty much everything that needs explaining, on to the other UI’s!




Custom Prefixes and Styles UI:


The Name Viewers give a list of all the prefixes and styles. You can select items the same way as the other viewers. Unlike the other viewers, it will only affect the focus of the viewer so selecting multiple will do nothing.

The Edit Boxes are where you can add or remove things. By clicking on a name, it will fill in the box with its name. Pressing Plus will add it to the list, Pressing Minus will remove it from the list.

Save will save the current lists of prefixes and styles

Exit will exit the program, make sure to save!



Preferences UI:


Edit colors is where you can make custom skins, you can share via the preferences.json in the data folder. The drop down lets you select what to edit, and the edit button will let you edit it.

Replace Duplicate Prefixes is a buggy feature that when appending a prefix to an already existing prefix, it will remove the original prefix if it's equal to the new one. Currently buggy, don’t mess with it.

Repair Nameless Presets will repair any presets missing the “preset_name” tag in it’s file, being mostly 1.0.3 and lower. On loading the files into the program, it will create the tag, but not apply it to the file. By pressing APPLY TO SELECTED, you will create the tag in it’s file. By unchecking this box, a list of problematic presets will appear at the startup of the program and they will not load into the viewers. 

Custom Whitespace Character is where you can set what you want the whitespace character for the Break Box to be. By typing the character set here into the Break Box, it will look for whitespace as the prefix divider. 

Default Break Character is what the Break Box will be set to on opening the program.

Save saves the current settings.

Reset to Defaults will reset all settings to default.

Exit will exit the window, remember to save!



FaQ:
How do I add a prefix to a bunch of presets?
Select all the presets you want, edit the prefix box and check the box next to it. Press APPLY TO SELECTED and it will append the prefix to every name.

How do I remove a prefix from a bunch of presets?
Like before, select the presets, but this time delete the contents of the prefix box and check the box next to it. Then press APPLY TO SELECTED.

How can I mass repair nameless presets?
Make a folder of all the problem presets in your Vital preset folder. Copy them into the PRESETS_HERE folder. Run the program, select everything, and press APPLY TO SELECTED. This will repair all of the presets. It will, unfortunately, append a ‘0’ to the end of the file and preset name. Why? EasyEdits will append a ‘0’ to the end of any duplicate file names to avoid OS conflict. I might try fixing this later, but I am exhausted from working on this for now :/

Why is the source code a couple Kb, but the application is 10Mb?
Pyinstaller! Python is pretty much just easy C, a programming language that all computers run. So in order to get python to run on a computer without python, pyinstaller needs to compile all of the libraries, including tkinter, which is a massive GUI library that I used to make this. If you need more information: https://www.pyinstaller.org/

When will this not be in beta?
When I decide to finish it :) This has been my biggest vital tool/python project ever and it was quite draining. I’m not sure if I have the energy to recode everything, so I might just fix bugs and then release it as is.

Can this do more than just add prefixes?
Yes! It can repair old vital files missing the “preset_name” tag, it can apply custom styles to a mass amount of presets, and it can edit all the other basic data in the file. However, this was built mainly for the prefixes and style changing, so you might find it a bit lacking in other ways.




Contact Me:
This should be everything! 
If you have any questions, feedback, bugreports, put them here!

The Vital Tools Discord server is where I post more frequent dev updates and where you can get help and feedback when making your own tools! It’s also open for beta testers and viewers.
