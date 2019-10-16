#  

## DIFFICULTIES: INFINITE SCROLLING PAGES ##

I found that the pages of photos are *INFINITE SCROLLING PAGES* which means I need to find a way to make the server give me the data.









## I SUCCEED!!!!!!!!!!!! ##

When I am writing down this markdown, my little cute crawler is downloading images from the Internet!!!

However, suddenly, an error came out: *TypeError: string indices must be integers*. I tried a lot and couldn't figure out what was wrong! In the end, I just tried to run `string = 'abcdefg' print(string[1,5])` and it still returned an Error! I realized that **It should be `sting[1:5]`!!!!** WHAT A MISTAKE!!!

Although I have solved so many errors, my crawler returned her last error, which happened after a folder of pictures have been downloaded, the function `.find(...)` returned -1 that meant no more things could be found. But to cut the slices of URLs, I used `.find(...) + 5` to make the head pin just at the head of the slices I wanted, which exactly led to the error. I let the `while` to judge if she need to continue, then use `+5`.

Finally, the pictures were successfully downloaded!!! 