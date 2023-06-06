import csv
import json
import sys


def main():
    # Verify inputs
    if len(sys.argv) < 3:
        sys.exit("Please input a minimum of 2 decklists")

    # open the AtomicCards database for reference
    with open('databases/AtomicCards.json', 'r', encoding="utf8") as f_database:
        # store as a global variable so other functions can reference it.
        global database
        database = json.load(f_database)

    # open cedh staple list for reference
    with open('databases/cedhstaples.csv', newline='') as f_staples:
        staplesreader = csv.reader(f_staples, delimiter=';')
        # store as a global list so other functions can reference it.
        global cedhstaples
        cedhstaples = []
        for row in staplesreader:
            cedhstaples.append(row[0])

    # store deck names and contents in a list of dictionaries
    # decks is our most important variable. it's where we store each deck, and result of each test. Every time we complete a test, we store the result in decks, and use that for our comparisons at the end
    decks = []
    for i in range(1, len(sys.argv)):
        decks.append({'deckname': sys.argv[i], 'decklist': deckdict("decklists/" + sys.argv[i] + ".csv")})

    # initialize variables
    averages = []
    overlapcount = []
    saltscores = []

    # for each decklist...
    # If we want to create any new tests, we do so here, and then append our decks variable with the result
    for j in range(len(decks)):
        # Calculate average mv decklist, and update the deck dictionaries and averages list with values
        deckAvgMV = avgMV(decks[j]['decklist'])
        decks[j].update({'MV': deckAvgMV})
        averages.append(deckAvgMV)

        # Calculate the overlap count, and update the deck dictionaries and overlap list with values
        competitive_count = cedhtest(decks[j]['decklist'])
        decks[j].update({'staplecount': competitive_count})
        overlapcount.append(competitive_count)

        # Calculate the salt score and saltiest cards, and update the deck dictionaries and salt score list with values
        saltresults = salttest(decks[j]['decklist'])
        decksaltscore = saltresults[0]
        saltiestcardname = saltresults[1]
        decks[j].update({'saltscore': decksaltscore})
        saltscores.append(decksaltscore)
        decks[j].update({'saltiestcard': saltiestcardname})

    # Calculate min an max scores for each test which can be used in determining pod health
    maxMV = max(averages)
    minMV = min(averages)
    maxStaples = max(overlapcount)
    minStaples = min(overlapcount)
    maxSaltScore = max(saltscores)
    minSaltScore = min(saltscores)

    # add color to our output.
    class color:
        PURPLE = '\033[95m'AA
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        ITALICS = '\033[3m'

    # organizes deck lists by mana value, then prints the decks out in that order.
    sorteddecks = sorted(decks, key=lambda d: d['MV'])
    print()
    print(color.BOLD + color.UNDERLINE + color.BLUE + "Average Mana Values:" + color.END)
    for k in range(len(sorteddecks)):
        print(sorteddecks[k]['deckname'], "has an average mana value of",  round(sorteddecks[k]['MV'], 2))
    print()

    # if decks all fall within a range *subject to change*, return a result, else test to see if there is an outlier, and suggest that deck make an adjustment
    print(color.BLUE + color.ITALICS + "Results:" + color.END)
    if maxMV - minMV <= .75:
        print("These decks should form a balanced pod based on their mana values")
    else:
        print("These decks are not balanced based on their mana values")
        if sorteddecks[1]['MV'] - sorteddecks[0]['MV'] >= .375:
            print(sorteddecks[0]['deckname'], "may want to consider switching to a slower deck")
        if sorteddecks[len(sorteddecks) - 1]['MV'] - sorteddecks[len(sorteddecks) - 2]['MV'] >= .375:
            print(sorteddecks[len(sorteddecks) - 1]['deckname'], "may want to consider switching to a faster deck")
    print()

    # organizes lists by cedh staple overlap, and prints the decks out in that order
    sorteddecks = sorted(decks, key=lambda d: d['staplecount'])
    print(color.GREEN + color.BOLD + color.UNDERLINE + "cEDH Database Overlap Count:" + color.END)
    for l in range(len(sorteddecks)):
        print(sorteddecks[l]['deckname'], "has", sorteddecks[l]['staplecount'], "cards in common with the cEDH databse")
    print()

    # if decks all fall within a range *subject to change*, return a result, else test to see if there is an outlier, and suggest that deck make an adjustment
    print(color.GREEN + color.ITALICS + "Results:" + color.END)
    if maxStaples - minStaples <= 20:
        print("These decks should form a balanced pod based on the number of competitive level cards present")
    else:
        print("These decks are not balanced based on the number of competitive level cards present")
        if sorteddecks[1]['staplecount'] - sorteddecks[0]['staplecount'] >= .20:
            print(sorteddecks[0]['deckname'], "may want to consider switching to a more competitive deck")
        if sorteddecks[len(sorteddecks) - 1]['staplecount'] - sorteddecks[len(sorteddecks) - 2]['staplecount'] >= .20:
            print(sorteddecks[len(sorteddecks) - 1]['deckname'], "may want to consider switching to more casual deck")
    print()

    # organizes lists by their salt score, and prints the decks out in that order.
    sorteddecks = sorted(decks, key=lambda d: d['saltscore'])
    print(color.PURPLE + color.BOLD + color.UNDERLINE + "Salt Scores:" + color.END)
    for m in range(len(sorteddecks)):
        print(sorteddecks[m]['deckname'], "has a total salt score of", round(sorteddecks[m]
                                                                             ['saltscore'], 2), "and its saltiest card is", sorteddecks[m]['saltiestcard'])
    print()

    # if decks all fall within a range *subject to change*, return a result, else test to see if there is an outlier, and suggest that deck make an adjustment
    print(color.PURPLE + color.ITALICS + "Results:" + color.END)
    if maxSaltScore - minSaltScore <= 20:
        print("These decks should form a balanced pod based on their salt scores")
    else:
        print("These decks are not balanced based on their salt scores")
        if sorteddecks[1]['saltscore'] - sorteddecks[0]['saltscore'] >= 10:
            print(sorteddecks[0]['deckname'], "may want to consider switching to a deck with more stax, control, or combo potential")
        if sorteddecks[len(sorteddecks) - 1]['saltscore'] - sorteddecks[len(sorteddecks) - 2]['saltscore'] >= 10:
            print(sorteddecks[len(sorteddecks) - 1]['deckname'], "may want to consider switching to a more pro-social deck")
    print()


def deckdict(deckname):

    # open list from command line arguments
    try:
        f = open(deckname, "r")
    except OSError:
        print("Could not open/read", deckname)
        sys.exit()

    with f:
        reader = csv.reader(f)

        # initialize a local list
        decklist = []

        # add card quantity and cardname to list
        for row in reader:
            if row[2] != 'Maybeboard' and row[2] != 'Sideboard':
                decklist.append({'quantity': int(row[0]), 'cardname': row[1]})

        return decklist


def avgMV(decklist):

    # initialize decks total mv, card count, and land count
    deckMV = 0
    cardcount = 0
    landcount = 0

    # for each card in the decklist, get the manavalue based on the cardname, add the quantity of the card to the total card count, and keep track of how many lands are in the deck
    for row in decklist:
        MV = manaValue(row['cardname'])
        deckMV += MV
        cardcount += row['quantity']
        if isLand(row['cardname']) == True:
            landcount += row['quantity']

    # returns the average manavalue of the deck, not inluding lands
    avgMV = float(deckMV / (cardcount - landcount))
    return avgMV


def manaValue(cardname):

    # search AtomicCards.json for MV based on card name
    manaValue = database['data'][cardname][0]['manaValue']
    return manaValue


def isLand(cardname):

    # Verifies whether ot not the card is a land, returns True or False. the 0 next to cardname only looks at the front half of the card, in the case of an MDFC, it will count the MV of the front side of the card.
    isLand = any(x == 'Land' for x in database['data'][cardname][0]['types'])
    return isLand


def cedhtest(decklist):

    # Calculates how many cards the deck has in common with the cEDH database
    overlap = 0
    for row in decklist:
        if row['cardname'] in cedhstaples:
            overlap += 1 * row['quantity']
    return overlap


def salttest(decklist):

    # Calculates the total salt score of the deck, and the saltiest card within the deck
    totalsalt = 0
    saltiestcardname = 'none'
    saltiestcardvalue = 0

    for row in decklist:
        cardname = row['cardname']

        # not all cards have salt scores, therefore the try function is necessary in case the salt score doesnt exist
        try:
            salt = database['data'][cardname][0]['edhrecSaltiness']
        except:
            salt = 0

        if salt > saltiestcardvalue:
            saltiestcardvalue = salt
            saltiestcardname = cardname

        # Accounts for decks that run multiple copes of the same card.
        totalsalt += (salt * row['quantity'])

    return totalsalt, saltiestcardname


main()