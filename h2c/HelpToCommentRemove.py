#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT REMOVE
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
#This script removes comment from selected node
#INSTALLATION:
#Place script inside $houdini/scripts folder

import hou

def main(kwargs):
    #node = kwargs["node"]
   
    for node in hou.selectedNodes():
        try:
            node.setComment("")
            node.setGenericFlag(hou.nodeFlag.DisplayComment,False)
            hou.ui.setStatusMessage("H2C: Comment removed from selected node.")
        except:
            hou.ui.setStatusMessage("H2C: Unable to remove comment from locked node: "+node.name())
  

main(kwargs)