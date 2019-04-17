def readMovieList(text_file):
    movie_list = []  # Empty list for later append movie dict into it
    # First, make all the lines in the text file into a list
    lines = [line.strip('\n') for line in text_file]
    # For every element in the list, create an empty venue dictionary
    for line in lines:
        venue = {}  # So that each line represent a new venue
        # for every line, split again, and everything inside it, split again
        for data in line.split("&"):
            key, value = data.split(":")
            # so that the key and venue will go into the dict respectively
            venue[key] = value
        movie_list.append(venue)  # Append the dict into the list
    return movie_list


# This function store user's sort result into text file.
def storeResult(file_name, movie_list, process_list):
    import datetime
    now = datetime.datetime.now()
    file = open("Result\\{0}_{1}.txt".format(file_name.replace(" ", "_"), now.strftime("%Y%m%d")), "w")
    file.write("------------------------------\n")
    file.write(" Movie Recommendation Service \n")
    file.write("------------------------------\n")
    file.write("Sort result stored at " + now.strftime("%Y/%m/%d %I:%M %p") + "\n\n")
    file.write("Below is your sort process:\n")

    bil = 1
    for x in process_list:
        for k in x:
            file.write(str(bil) + ". " + k + ": " + str(x[k]) + "\n")
        bil += 1

    file.write("\nBelow is your final sort result:\n")

    bil = 1
    for x in movie_list:
        file.write(str(bil) + ". " +
                   x["name"] + "  |  " +
                   x["genre"] + "  |  " +
                   x["rating"] + "  |  " +
                   x["year"] + "  |  " +
                   x["month"])
        bil += 1
        file.write("\n")

    file.close()


# Read genre text file and append into list
def readItemFile(text_file):
    genre_list = text_file.read().split("\n")
    return genre_list


# Sort movie list by genre or year or month
def sortGenreOrDate(movie_list, sort_type, option):
    new_list = []  # new movie list
    for x in movie_list:
        # Only split if applicable (in this case only genre), will become a list.
        whatever_list = x[sort_type].split(",")
        for z in whatever_list:
            if option == z:
                new_list.append(x)  # append after sort into new movie list.
    return new_list


# Sort by rating, only show movies where rating is above user input.
def sortRating(movie_list, rate):
    new_list = []  # new movie list
    for x in movie_list:
        if float(x["rating"]) >= float(rate):
            new_list.append(x)  # append after sort into new movie list.
    return new_list


# Record user's process of sorting the program.
def storeProcess(process_list, key, value):
    temp = {key: value}
    process_list.append(temp)
    return process_list


# This function check if movie list is empty after each sorting process.
def checkEmpty(movie_list):
    if not movie_list:  # If movie list is empty:
        return False
    else:
        return True
