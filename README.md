# Watch Your Profanity
---
##### Disclaimer: All the profane tweets used in the code are fictional. Any resemblance to already existing tweets is purely coincidental. Other non-profane tweets are taken from random datasets from around the internet.
---

The following program tries to calculate the degree of profanity in individual tweets from a file using a list of profane words stored in another file.
Degree of profanity is calculated using the following formula:

$x =$ Degree of profanity, <br />
$a =$ Number of slurs appear in the tweet, <br />
$b =$ Total number of words in the tweet

$$ x = {a \over b} \times 100 $$

### Files
- the_program.py: Python program that does the actual creation and generates results.txt
- slurs.txt: List of slurs used in the program
- tweets.txt: List of tweets used in the program
- results.txt: Final result in the following format

           Tweet: [TWEET]
                word count: [WORD COUNT OF TWEET], slur count: [NUMBER OF TIMES SLUR WORDS HAVE APPEARED]
                degree of racial profanity: [PERECENTAGE APPEARANCE OF SLUR WORDS (upto 2 decimal places)]

### Assumptions
- Degree of profanity is the percentage of appearance of slur words in the tweet
