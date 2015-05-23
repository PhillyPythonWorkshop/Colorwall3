#!/usr/bin/env python

#Look at the comments to see what this code is doing

#argparse & sys are two Python libraries being imported
import argparse, sys

#wall and effects are two of our other Python scripts
#the entire effects file is being imported
#Only the Wall class from the wall file is being imported
from wall import Wall
import effects


if __name__ == "__main__":
    #If we don't know what a command or function does we can look it up in the docs.
    #Looking up argparse.ArgumentParser() takes us to:
    #https://docs.python.org/2/library/argparse.html

    parser = argparse.ArgumentParser()
    #When we run the script from the command line,
    #we can give it some additional arguments as defined here.

    parser.add_argument("-w", "--width", type=int,
                        action="store", dest="width",
                        default=8, help="wall width")
    parser.add_argument("-t", "--height", type=int,
                        action="store", dest="height",
                        default=8, help="wall height")
    parser.add_argument("-e", "--effects",
                        nargs='+', dest="effects",
                        help="specific effects you wish to run")
    args = parser.parse_args()

    #We set a variable called wall 
    #which takes the class Wall (imported above) 
    #and calls it with either default width & height or 
    #whatever width and height we defined in the args as above
    wall = Wall(args.width, args.height)

    #If an effects arg was defined, use it for effects_to_run
    #Otherwise run all effects from the effects script imported above
    #Save this in a variable called effects_to_run as a list

    if args.effects:
        effects_to_run = [getattr(effects, a) for a in args.effects \
                              if hasattr(effects, a)]

    else:
        effects_to_run = effects.Effects

    #Loop through effects to run
    #Print that effect's name in the Python terminal
    #Run that effect in the Tkinter window 

    for effect in effects_to_run:
        new_effect = effect(wall)
        print(new_effect.__class__.__name__)
        new_effect.run()
