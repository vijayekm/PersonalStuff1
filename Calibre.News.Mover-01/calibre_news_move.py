#-------------------------------------------------------------------------------
# Name:        calibre_new_move
# Purpose:
#
# Author:      vijayekm
#
# Created:     17/04/2020
# Copyright:   (c) vijayekm 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from xml.dom.minidom import parse, parseString
import os
import shutil

#IN_DIR = "..\\tmp\\inebs\\"
IN_DIR = os. environ['USERPROFILE'] + "\\Calibre Library\\calibre\\"

OUT_DIR = "..\\tmp\\out\\"

def __discover_dc(opf_xmldoc, name, first_only=True):
    value = None
    try:
        if first_only:
            node = opf_xmldoc.getElementsByTagName(name)[0].firstChild
            if node:
                value = node.nodeValue
        else:
            value = [n.firstChild.nodeValue for n in opf_xmldoc.getElementsByTagName(name) if n.firstChild]
    except (KeyError, IndexError):
        pass
    if not value:
        tag_name = 'dc:{}'.format(name)
        try:
            if first_only:
                node = opf_xmldoc.getElementsByTagName(tag_name)[0].firstChild
                if node:
                    value = node.nodeValue
            else:
                value = [n.firstChild.nodeValue for n in opf_xmldoc.getElementsByTagName(tag_name) if n.firstChild]
        except (KeyError, IndexError):
            pass
    if first_only:
        return value.strip() if value else value
    else:
        return [v.strip() for v in value]

def _discover_publication_date(opf_xmldoc, date_html=None):
    date = __discover_dc(opf_xmldoc, 'date')

    if not date and date_html is not None:
        date = _find_publish_date_from_dom(date_html)

    return date

def getModifiedPath(dst) :

    if not os.path.isdir(dst) :
        return dst

    num = 0

    while True:
        num +=1
        modDst = dst+ str(num).zfill(4);

        if not os.path.isdir(modDst) :
            return modDst

def moveDir(path,dstDir):

    if not os.path.isdir(dstDir):
        os.mkdir(dstDir)

    if not os.path.isdir(dstDir):
        print("Could not open find or create dir " +dstDir)
        return

    dirNamePart = os.path.basename(path);

    dirNamePart = dirNamePart.replace("(Web)","Web");

    if dirNamePart.find("(") :
        dirNamePart = dirNamePart.split("(") [0]

    dirNamePart = dirNamePart.replace(" ",".");
    dst = dstDir +"\\" + dirNamePart

    dst = getModifiedPath(dst)
    destination = shutil.move(path, dst)

    #exit(0)

def processDir(path):
    #print "Processing Dir"  + path
    metaFile = path +"\\"+"metadata.opf"

    if  not os.path.isfile(metaFile)  :
        print ("Metafile does not exist "  + metaFile)
        return

    dom1 = parse(metaFile)
    dt = _discover_publication_date(dom1)

    if dt == None:
        print ("Could not get the date for " + path)
        return

    d, t = dt.split('T')
    print("The date is " + d)
    dstDir = OUT_DIR+"\\"+d

    moveDir(path,dstDir)

def main():
    for filename in os.listdir(IN_DIR):
        path = IN_DIR+filename

        if(os.path.isdir(path)) :
            processDir(path)

if __name__ == '__main__':
    main()
