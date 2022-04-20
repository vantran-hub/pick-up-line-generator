import streamlit as st
import praw
import pandas as pd
import numpy as np

st.title("Pickup Line Generator")
st.subheader("Source: Reddit r/pickuplines")


reddit = praw.Reddit(client_id='IAjSKHOQQQxV6B6V1uURJA', 
                     client_secret='I6ZzUJ_YEztDSI8UxSvgliusy7c0Xw', 
                     user_agent='pick up lines')

posts = []
sub = reddit.subreddit("pickuplines")
for post in sub.hot(limit=900):
    posts.append([post.title, post.score, post.selftext])
posts = pd.DataFrame(posts,columns=['title', 'score', 'body'])
posts["lines"] = posts["title"] + ' ' + posts["body"]
posts = posts[["lines","score"]]

#delete the megathread and duplicated rows
posts.drop([posts.index[0]],inplace=True)
posts.drop_duplicates(subset=['lines'])

@st.cache
def grab_puline (df):
    randomline= np.random.choice(607, replace = False, size = 1)
    return df.iloc[randomline]

lines_only=pd.DataFrame(posts['lines'])
df=lines_only
result=grab_puline(df)
result1=result.to_string(index=False,header=False)
st.write(result1)

