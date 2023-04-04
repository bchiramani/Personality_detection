
import instaloader
from datetime import datetime

persons=[

#names of public users

]


L = instaloader.Instaloader()
L.load_session_from_file("amani_amounnn")
UNTIL = datetime(2021, 3, 30)
SINCE = datetime(2017, 3, 30)


for person in persons:
    print("Downloading for person: "+ person+"\n")
    posts = instaloader.Profile.from_username(L.context, person).get_posts()
    filtered = filter(lambda post: SINCE<post.date<UNTIL, posts)
    if not filtered:
        #Person has no posts in specified date range.
        no_posts_in_range_file = open("no_posts.txt","a")
        no_posts_in_range_file.write(person+"\n")
        break
    for post in list(filtered):
        print(SINCE<post.date<UNTIL)
        output = L.download_post(post, person)
        print(output)
    print("Done downloading for ", person, ". Adding to done list.")
    #File that keeps track of scrapped profiles.
    done_list = open("done.txt","a")
    done_list.write(person+"\n")
