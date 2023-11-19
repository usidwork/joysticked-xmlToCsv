
import xml.etree.ElementTree as ET
# -----------------------------------------------------------------------
# GamesExtraction ver 2.1
# revision 10
# Coded by usworks.
# Tested on Python ver 3.9.12 (ubuntu 22.2 + Windows 10)
# will find the Games description where cloneof = ""
# -----------------------------------------------------------------------
# :: Required ::
# Python ver 3.9 above
# ------------------------------------------------------------------------
# place the xml file in same folder where python program is placed
# folder should have writepermissions for current user.
# to run open command prompt and type following
# >python GameXmlExtraction.py


def GetGameName():
    try:
        tree = ET.parse('MAME.xml')
        root = tree.getroot()
        extractedTitle = {}
        with open("Game.csv", "w", encoding="utf8") as file:
            itercntr = 1
            for itemgame in root:
                print("Processing xmlrecord # " +
                      str(itercntr), end="\r", flush=True)
                itercntr = itercntr+1
                if itemgame[1].tag == 'cloneof' and itemgame[1].text == None:
                    file.write(str(itemgame[0].text).strip() + "\n")
                    # "," + str(itemgame[1].text).strip() + "\n")
    except Exception as ex:
        print("Error: " + str(ex))


def main():
    print("----------------------- Get Game Names-------------(Coded by usworks)-----------------\n")
    print("--------------------------------------------------------------------------------------\n")
    print("---------------------------------------------------------------------------------------\n")
    print("Please Wait starting processing ........  \n")
    GetGameName()
    print("\n ************* Completed Processing all data. *************** \n\n\n")


if __name__ == "__main__":
    main()
