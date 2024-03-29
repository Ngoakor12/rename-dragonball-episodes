# rename-dragonball-episodes

## Explainer/demo video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/A1pkb1z_BsQ/0.jpg)](https://www.youtube.com/watch?v=A1pkb1z_BsQ)

## problem

I have a lot of Dragonball episodes, each within its series folder(E.g., dragonball super) with inconsistent file names. This is a problem because finding and playing each series in the right order is very difficult.

## solution

Instead of going to each folder and renaming each file individually via the GUI. Create a script to go to each series folder and mass rename the episode files in a specific and consistent filename pattern that is easy to follow.

## input(s)

A list of Dragonball series folders with inconsistently named episode files in each folder

## output(s)

An updated list of Dragonball series folders with consistently named episode files in each folder

The desired filename pattern is "db-{optional series acronym}-{episode number}.{extension}"

Examples:

dragonball

- `Dragonball 001 - The Secret Of The Dragon Balls.mkv` -> `db-001.mkv`

dragonball z

- `Dragonball Z 182 - Gohan's Plea.mkv` -> `db-z-182.mkv`
- `Episode 159.MP4` -> `db-z-159.mp4`

dragonball z kai

- `Dragon ball Z kai 117.mp4` -> `db-z_kai-117.mp4`
- `Episode 167.MP4` -> `db-z_kai-167.MP4`

dragonball gt

- `Dragonball GT 32 The Return Of Uub.mkv` -> `db-gt-032.mkv`

dragonball super

- `dbzwhisrocks.blogspot.com.DBS.Dubbed Ep 028.MP4` -> `db-super-028.mp4`

## potential steps to take

Loop through each folder.

- extract the series name from the folder name

Loop through each file.

- extract the episode number from the file name
- create the desired file name
- rename the existing episode file with the desired file name

# multi-part project

This is the same project above, separated into parts.

## part 1 - file names

Given a list of file names and the series name as input, return a list of file names in the desired format.

## part 2 - file names - folder as source

Upgrade your script so that a folder path to the list of episodes is given as input instead. The series name should be taken from the provided folder name. Return a list of file names in the desired format.

## part 3 - rename files - one folder

Upgrade your script to rename files instead of returning a list of desired file names.

## part 4 - rename files - multiple folders

Upgrade your script so that a list of folder paths with the list of episodes is given as input instead. The series names should be taken from the provided folder names. Return a list of file names in the desired format.

## part 5 - rename files - non-destructive update

Make use of command line args to indicate the target folder to save your newly renamed files in the right folder structure instead of destructively renaming the files.
