# use the pretty print library to better visualize data
import pprint
pp = pprint.PrettyPrinter(indent=3)

# working with our original file - topPlayers.txt
topPlayers = "topPlayers.txt"

# use a list to read the file into the program
scoreList = []

# sort data and read original file
# open file in read only mode
with open(topPlayers, "r") as myFile:
    # separate our data from fixed width file by position
    for line in myFile.readlines():
        score = line[0:10]
        name = line[10:20]

        # as we break out each field, add them to our list
        # formatting - use rstrip to delete extra space and new line from each entry
        scoreList.append((score.rstrip(" "), name.rstrip("\n")))
    myFile.close()


# define a function to create & update a new file with the top scores
def updateFile(newScore, newName):
    # write to the new file
    topPlayersOut = "topPlayersOut.txt"
    newFile = open(topPlayersOut, "w")

    # add each new entry to original info broken out earlier
    scoreList.append((str(newScore), newName))

    # sort by the 0th element of each row
    scoreList.sort(key=lambda x: int(x[0]))

    # keep only top 5 entries and delete rest
    del scoreList[5:]

    for eachScore in scoreList:
        # write to file each score position 0 to 10 and each name position 10 to 20
        # *eachScore makes the tuples unpack into separate arguments
        newFile.writelines('{:10s}' '{:10s}'.format(*eachScore))
        newFile.writelines("\n")

    # close the file
    newFile.close()

    # show user the leaderboard
    print(f"\n======= Top 5 Players =======")
    pp.pprint(scoreList)

