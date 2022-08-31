def open_file_return_list(loc):
    """
    Summary:
        Method to open the file name passed and return its content as list
        Used to generate list objects for slur words and tweets that would be used in the program
    Parameters:
        loc: (str) file location
    Returns:
        _list: (list), list object containing the contents of the file
    """
    
    _list = []
    with open(loc, "r") as _file:
        for line in _file:
            _list.append(line.strip("\n"))
    return _list

def main():
    """
    Summary:
        The main method
    Parameters:
        n/a
    Returns:
        n/a
    """
    
    #list of slurs and tweets
    slurs = open_file_return_list("slurs.txt")
    tweets = open_file_return_list("tweets.txt")
    
    #opening result file to write in it
    result = open("results.txt", "w")

    for tweet in tweets:
        #counting the number of times slur words have appeared in the tweet
        slur_count = 0
        for slur in slurs:
            slur_count = slur_count + tweet.count(slur)
        
        #degree of racial profanity is assumed to be the percentage(upto 2 decimal places) of appearance of slur words per tweet
        degree_profanity = "{:.2f}".format(( slur_count / len(tweet.split()) ) * 100)
        
        """
            writing result in results.txt in the following format,
            Tweet: [TWEET]
                word count: [WORD COUNT OF TWEET], slur count: [NUMBER OF TIMES SLUR WORDS HAVE APPEARED]
                degree of racial profanity: [PERECENTAGE APPEARANCE OF SLUR WORDS (upto 2 decimal places)]
        """
        result.write(f" Tweet: {tweet} \n\t word count: {len(tweet.split())}, slur count: {slur_count} \n\t degree of racial profanity: {degree_profanity}% \n\n")

#invoking main()
if __name__ == "__main__":
    main()
