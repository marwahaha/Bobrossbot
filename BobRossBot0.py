import praw
import pdb
import re
import os
import time
import random
from datetime import datetime
import sys
print("logging in")
reddit = praw.Reddit(user_agent='Bob Ross Bot v0.1',
                  client_id='g-gEG3suRUmjCg',
                  client_secret='_kjQZs-lv7Po7qXiRl_sgfEYoc8',
                  username='BobRossBot_',
                  password='0110101')
# Quotes taken from: http://bobrossquotes.com/quotes.shtml
from setuptools.command.rotate import rotate
print("loading quotes")
ross_quotes = \
[
" Trees cover up a multitude of sins.",

" Remember our Golden Rule: A thin paint sticks to a thick paint. ",

" And that makes it look like birch trees, isn't that sneaky? Heh. Ha. It's gorgeous. ",

" Be sure to use odorless paint-thinner. If it's not odorless, you'll find yourself working alone very, very quick. ",

" Let's just blend this little rascal here, ha! Happy as we can be. ",

" Clouds are very, very free. ",

" Decide where your little footy hills live. ",

" Shwooop. Hehe. You have to make those little noises, or it just doesn't work. ",

" Try to imagine that you are a tree. How do you want to look out here? ",

"  You know me, I gotta put in a big tree. ",

" Gotta give him a friend. Like I always say 'everyone needs a friend'. ",

"  Any time ya learn, ya gain. ",

"  Just put a few do-ers in there... ",

"  Maybe in our world there lives a happy little tree over there. ",

"  You can do anything you want to do. This is your world. ",

"  You can put as many or as few as you want in your world. ",

" That's a crooked tree. We'll send him to Washington. ",

" I like to beat the brush. ",

" In painting, you have unlimited power. You have the ability to move mountains. You can bend rivers. But when I get home, the only thing I have power over is the garbage. ",

" You need the dark in order to show the light. ",

" Look around. Look at what we have. Beauty is everywhere—you only have to look to see it. ",

" There's nothing wrong with having a tree as a friend. ",

" There's nothing wrong with having a tree as a friend. ",

" They say everything looks better with odd numbers of things. But sometimes I put even numbers—just to upset the critics. ",

" How do you make a round circle with a square knife? That’s your challenge for the day. ",

" How do you make a round circle with a square knife? That’s your challenge for the day. ",

" I remember when my Dad told me as a kid, ‘If you want to catch a rabbit, stand behind a tree and make a noise like a carrot. Then when the rabbit comes by you grab him.’ Works pretty good until you try to figure out what kind of noise a carrot makes… ",

" We tell people sometimes: we're like drug dealers, come into town and get everybody absolutely addicted to painting. It doesn't take much to get you addicted. ",

" The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. As long as you believe. ",

" Water's like me. It's laaazy ... Boy, it always looks for the easiest way to do things ",

" Oooh, if you have never been to Alaska, go there while it is still wild. My favorite uncle asked me if I wanted to go there, Uncle Sam. He said if you don't go, you're going to jail. That is how Uncle Sam asks you. ",

" I really believe that if you practice enough you could paint the 'Mona Lisa' with a two-inch brush. ",

" If I paint something, I don't want to have to explain what it is. ",

" We artists are a different breed of people. We're a happy bunch. ",

" We don't make mistakes. We just have happy accidents. ",

" We don't make mistakes. We just have happy accidents. ",

]
print("quotes loaded")
username = "BobRossBot_"
print("setting subreddit parameters")
subreddit = reddit.subreddit("all")


print("finding comment")
for comment in subreddit.stream.comments():
    if re.search("Bob", comment.body, re.IGNORECASE):
       print("comment found!")
       print("preparing quote.")
       ross_reply = random.choice(ross_quotes)
       comment.reply(ross_reply)
       print("replied with quote!")
       print("cooldown")
       print("waiting 2 seconds")
       print("restarting")
# Created by /u/whaliam
# 6Ep96ck9@protonmail.com
