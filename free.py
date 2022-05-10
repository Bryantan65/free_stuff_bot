import praw
import webbrowser
from win10toast_click import ToastNotifier # Desktop Notificaion library

print('This program will get the 1st new result from R/FREE')

# Initialize reddit API
reddit = praw.Reddit(
    client_id="jb1H8L6HWRSieBRRSp8owA",
    client_secret="7X3_dEXztNoWT_HIDKV0hwSubOBeSw",
    user_agent="windows:www.reddit.com by(u/FrozenMallets)",
)
subchosen = 'FREE'
#input('What sub do you want to track? r/? ')
oldPost = ''



while True:
    # for each new submission in the subreddit FREE
    for submission in reddit.subreddit(subchosen).new(limit=1):
        if submission != oldPost:
            posttitle = submission.title
            posturl = submission.url
            print(posttitle)
            def open_url():
                try:
                    webbrowser.open_new(posturl)
                    print('Opening URL...')
                except:
                    print('Failed to open URL. Unsupported variable type.')

            toaster = ToastNotifier()
            toaster.show_toast(
                posttitle,                                   # title
                "Click to open URL! >>",                     # message
                icon_path='D:/OSSU/free_stuff_bot/among_us_reddit_icon_156923.ico', # 'icon_path'
                duration=5,                                  # Popup duration, seconds, None = leave in Notification Center
                threaded=True,                               # True = run other code in parallel;
                                                             # False = code execution will wait till notification disappears
                callback_on_click= open_url                  # click notification to run , cannot use webbrowser.open here
                )
            # store the name of newest post in oldPost var, when the loop runs again, it will check if new post is == old
            oldPost = submission
        else:
            pass




