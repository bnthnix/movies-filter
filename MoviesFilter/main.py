# Import necessary python files
import function
import progInput
import output

start = True
# The while loop below enable to availability to restart the program.
while start:
    # Import necessary files from the start of program.
    movieFile = open("List\\movieList.txt", "r")
    movieList = function.readMovieList(movieFile)
    movieFile.close()
    # -----
    genreFile = open("List\\genreTypes.txt", "r")
    genreList = function.readItemFile(genreFile)
    genreFile.close()
    # -----
    monthFile = open("List\\monthList.txt", "r")
    monthList = function.readItemFile(monthFile)
    monthFile.close()
    # -----
    yearFile = open("List\\yearList.txt", "r")
    yearList = function.readItemFile(yearFile)
    yearFile.close()
    # -----

    output.welcomeBanner()  # To print the welcome banner.

    # Initialize necessary variables
    sortType = ""
    userInput = ""
    process = 0
    processList = []
    #historyList = [movieList]  # Initialize sort history records #Not used.
    # -----

    while True:
        # Get user selection
        output.userSelection()
        userSelection = progInput.getSortSel()

        # Sort by Genre
        if userSelection == "A" or userSelection == "a":
            sortType = "genre"
            output.printMenu(sortType)
            # Get user to input genre type.
            userInput = progInput.getGenreOrDate(genreList, sortType)
            # Sort the movies according to the genre type.
            movieList = function.sortGenreOrDate(movieList, sortType, userInput)

        # Sort by Rating
        elif userSelection == "B" or userSelection == "b":
            sortType = "rating"
            # Get user to input rating.
            userInput = progInput.getRating()
            # Sort out the movies that has less rating than user input.
            movieList = function.sortRating(movieList, userInput)

        # Sort by Year
        elif userSelection == "C" or userSelection == "c":
            sortType = "year"
            output.printMenu(sortType)
            # Get user to input year.
            userInput = progInput.getGenreOrDate(yearList, sortType)
            # Sort the movies according to the year.
            movieList = function.sortGenreOrDate(movieList, sortType, userInput)

        # Sort by Month
        elif userSelection == "D" or userSelection == "d":
            sortType = "month"
            output.printMenu(sortType)
            # Get user to input month.
            userInput = progInput.getGenreOrDate(monthList, sortType)
            # Sort the movies according to the month.
            movieList = function.sortGenreOrDate(movieList, sortType, userInput)

        # Quit the Program
        elif userSelection == "Q" or userSelection == "q":
            start = False
            break

        # Store sort result
        elif userSelection == "S" or userSelection == "s":
            if process > 0:
                fileName = ""
                while fileName == "":
                    # Get user to input file name
                    fileName = progInput.getFileName()
                # Store result to file
                function.storeResult(fileName, movieList, processList)

                # Ask if user want to restart program or not
                start = progInput.getRestart()
                break

            # Run if user want to store result at the beginning of the program.
            else:
                output.printString(0)
                # Ask if user want to restart program or not
                start = progInput.getRestart()
                break

        # Line below store sorting process into processList
        processList = function.storeProcess(processList, sortType.title(), userInput)

        # Line below outputs sorted process(es)
        output.printProcess(processList)

        # Line below check if movieList is empty
        x = function.checkEmpty(movieList)
        if x:
            # Line below outputs sorted result
            output.printSorted(movieList)

        else:
            output.printString(1)

            # Ask if user want to restart program or not
            start = progInput.getRestart()
            break

        process += 1

# Print quit banner
output.quitBanner()
