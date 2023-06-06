# Casual Commander Deck Comparisons
#### Video Demo: https://www.youtube.com/watch?v=SAP9t9dOJOM

#### Description:

Abstract:
    I wrote this program to take decklists for the commander variant of the game Magic: the Gathering as inputs, and determine whether or not the decks will form a balanced pod.

The three tests:
    There are many different factors that can determine whether or not the decks present in a pod are balanced, and in this project's current iteration, the program runs 3 tests to determine how well the decks will play against one another.
        The first test determines the average mana value of each deck:
            Every spell in a deck has a cost to cast the spell which is paid for by the games resource system, mana.
            The mana value of a card is determined by how much mana you have to spend in order to cast the card.
            In general, faster decks have a lower average mana value because a low mana value means you are able to impact the game early and often.
            Conversely, more casual decks will have a higher average mana value, and the decks will begin to develop later in the game, and usually will cast fewer spells each turn.
            This first test checks to see if all decks in a pod have around the same mana value, and if not, it will make a suggestion on what changes can be made to create a better game.
        The second test checks how many competitive level card each deck plays:
            While commander is generally a casual game, there is a large community of competitve players who look to build the strongest decks possible.
            They have compiled a list of what are called "staple cards" which are cards that show up most often in a game of competitive commander.
            This second test checks each decklist against the competitive staples database, and determines how much overlap is present.
            If one deck is running has a higher or lower quantity of competitive cards, the program will suggest that that person changes decks in order to promote a better game
        The third test determines the salt score of each deck:
            With Magic's huge library of cards, there are some cards that people simply don't like playing against.
            In 2019, a commander data and deck building website conducted a poll where participants voted on which cards they least like to play against in a game of commander by giving the cards a salt score.
            Cards received a salt score from 0-4, where 0 meant people had no issue when others played it, and 4 means that it was a card that ruins their game experience when they see it played.
            This poll is updated each year, and in the most recent poll of 2022, over 3,000,000 votes were tallied.
            This test takes the salt score of each card in a deck, and adds them together to give the deck a total salt score, and this test makes sure that each deck is playing a similarly social deck.
            For more information on salt scores, go to this link: https://edhrec.com/articles/new-edhrec-feature-salt/

How to use the program:
    Step 1: ensuring the MTG library is up-to-date.
        I used mtgJSON as a resource which compiles a ton of information on each card to help run all of the tests.
        Since Wizards of the Coast (the company that produces Magic: the Gathering) prints new cards that are added to the game regularly, I wrote a simple program called 'update.py' which ensures the library is up-to-date.
        The mtgJSON database is only updated once per day, and they ask that users only make 'calls to their server' as necessary, and then store the information locally, as to reduce traffic.
        So before you begin using the program run 'update.py' to ensure the library of cards is up to date.
    Step 2: populate the decklist folder.
        Decklists must be in a csv format where the first column is the quantity of the card in the deck, the second column is the name of the card, and the third column is the category of the card.
        This can easily be done using Archidekt.com, which is a MTG deck building website.
        Starting from a decklist in Archidekt:
            1 click export on the bottom left pannel
            2 change file type to csv
            3 select 'Quantity' 'Name' and 'Category' in Included Fields
            4 Select Download in the bottom right of the page
            5 Drag the file to decklists folder in the prgram
            6 (optional) rename the file to your liking; for simplicity, avoid spaces (the program uses command line arguments, so if there are spaces in name, quotation marks will need to be used around the decklist to avoid errors)
    Step 3: Run the program
        After all decklists have been populated in the decklist folder, you can run the program with the names of the decklist as command line arguments.

Step by step tutorial:
    1 Open up a new terminal
    2 type 'CD project' in the terminal and hit ENTER
    3 type 'python update.py' and hit ENTER
        it should return the message 'File succesfully updated' when complete
    4 type 'python project.py' followed by the name of each decklist present in the pod, then hit ENTER
        IMPORTANT: If the you have 2 decks titled ABC.csv and XYZ.csv, you would just write 'python project.py ABC XYZ' then hit enter - 'decklist/ABC' and 'XYZ.csv' will return errors
        If you receive an error, make sure the deck list name matches the command line argument, and make sure the list is in the correct 'decklists' folder
        Most games of commander have 4 players, but this program will work with as few as 2 decklists.
    Provided there are no errors, the program will give you the results of each test and subsequent suggestions if it detects the pod may be imbalanced based on the inputs.


Understanding Magic: the Gathering:
    For those unfamiliar with Magic: the Gathering, this section is intended to help you understand why this program may be useful.
    Magic: The Gathering is a collectible card game (in fact, it was the first collectible card game) where the point of game is to build a deck made up of spells, creatures, and lands that work together to win the game
    Since its inception in 1993, they have printed over 25,000 unique cards, and they print new cards every few months.
    There are many different ways to interract with this cardgame through different formats (modern, legacy, standard, pauper), each of which has it's own unique rule set and card pool.
    The most popular format today is called commander or EDH, and it is different from most all other formats in one very specific way, it is a casual format.
    Casual formats differ from competitive formats in that casual formats primary purpose is not to build the strongest, most powerful deck, but rather to show creativity and self expression.
    Since the goal of Casual commander is centered less around winning, and more around having an enjoyable game, it is important that each player brings a deck that is at a similar power level to each other deck at the table.
    In general, you play against your friends, and this is a self regulating system, but with covid, people were less able to meet up with their freinds to play, and instead turned to playing the game online.
    This leads to a lot of times playing games against people and decks you have never met before, and it can be difficult to determine whether your deck will play well against the others in the pod.
    This project looks to address that problem.

DISCLAIMER:
    this program will not guarantee a good game.
    Games that this program suggests will be imbalanced may turn out great, and games that this program suggests are balanced may not go well.
    There are too many factors to account for everything, and too much randomness within the game to be a perfect predictor.
    This program just looks to provide data to help facilitate pre-game conversations, and minimize the instances of imbalanced games.
    People should understand their decks, and know which tests may not apply very well to their decklists.
    For example: there are many decks whose goal is to cheat in big and powerful spells (reanimator strategies, polymorph effects, etc.), and these decks will often have higher Average Mana Value results.
    This test may suggest that the decks switch to a faster deck, but in practice, a person should recognize that this test is not a good indicator for the strategy, and ignore the suggestions.

The journey of this project:
    As an avid magic player, and someone who has experienced many imbalanced games since covid forced us to begin playing online, I knew that there was a need for something like this in the community.
    Originally I was going to try to write code that gave decklists a 'power level' and then determine whether or not a pod was balanced.
    I would determine the power level of each deck by looking at the top 1000 most played cards in commander, and giving each one a weight
    I would also go over the top 100 commanders, and give them a multiplier based on how strong they are.
    There are a few issues with this approach:
        The program is not future proof - as more cards and commanders are printed, I will have to constantly update their weights, and as the meta shifts, I will have to adjust old weights and multipliers
        The program is heavily influenced by input bias - I as the programmer has to determine what is 'strong' and what is 'fun'
    So, I spoke with a lot of people in the commander community, and we together determined what would be beneficial:
        Run tests that are objective - people get defensive when they hear their deck is anything other than a power level 7, but if we instead return things like the decks cEDH staple count, people can digest that better
        Give people the results - I was originally opposed to this as I just wanted the program to return suggestions, but I realized that by giving results, people have a better context of how their decks look compared to others
        Run more than one test - there are so many factors that can lead to a game being good or bad; the more tests that are run, the better conversations people can have before a game begins

What I learned:
    A LOT!
    I had no programming experience prior to this course, and even after I completed all of the lessons, there was still a lot that came up that I had to learn how to approach.
    For example:
        Navigating large json file
        Reading a file from a website, and save the information locally
        Working with command line arguments, and debugging them
        Using built in features to python such as sorting and adding font adjustments
        Organizing code so that I could make adjustments to it later
    One of the greatest moments was being able to use my program in real life.
    I had everybody send me their deck list, and within a few minutes, I was able to share the results, and one player actually swithced decks to better match everyone else.


The future of this project:
    I plan to continue growing as a programmer, and as I get better, I could see myself writing many more tests that could be a good indicator of pod health
    One test that I tried to write, but was not yet equipped to approach is determining the budget of each deck.
    One great determination of balance is making sure all decks in a pod cost roughly the same amount.
    Some of the strongest cards in magic cost hundreds of dollars, and this would ensure everyone is on a similar playing field.
    The test would also not take into consideration which version of the card someone is running.
    A card like 'Sol Ring' has been printed 68 different times with the cheapest version costing around $1.50 and the most expensive version costing over $850.
    Regardless of which version of the card you play, they each do the exact same thing, so I want the budget of the deck to just look at the cheapest version available of each card.
    When I tried to implement this test, I ran into a few issues
        1 The pricing file does not use 'cardname' at all, instead, it uses a unique id for each printing of a card
        2 The pricing database is over a gigabyte of text, and the program crashed every time I triend to read into it.
        3 The file type is '.json' and I could not figure out how to read that into a '.db' file type so I could use SQL to help determine the budget.
    There are ways to work around these hurdles, the ijson library can help with the size issue, and gaining experience with mySQL could help with the file type
    I do plan on implementing this at somepoint once I am better equipped
    I could aslo see about making this program more user friendly by making a website.
    Rather than having people upload decklists, they could just copy and paste links to their decklists, and use the Beautiful Soup library to scrub those links to create lists that the program can read
    I'm excited that this is something I can continue to develop even after I complete this course.

Shout Outs:
    Thank you to mtgJSON for providing an incredible database of Magic cards
        Copyright © 2018 – Present, Zach Halpern, Eric Lakatos
    Thank you to Justin for providing guidance and resources on how to tackle issues, and brainstorming ideas for the project.
    Thank you to Micah, Chappy, T-Coats, Ryan, and all the members of the Legendary Creature Podcast and Playing with Power Discord channels for helping me brainstorm ideas
    Thank you to Colin, Cam, Jeffrey, Lenny, Keaton, Russel, Shane, and everybody else who sent me decklists to help test my code.