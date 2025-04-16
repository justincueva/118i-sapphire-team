import streamlit as st
import praw # type: ignore
import openai
import os

# Set your OpenAI API key (safely stored as an environment variable or use st.secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="reddit_sentiment_app"
)

st.title("📊 Reddit Sentiment Analyzer")
st.markdown("Analyze sentiment of recent Reddit posts from a specific subreddit or keyword.")

# Input selection
subreddit_name = st.text_input("Enter Subreddit (default is 'SanJose'):", value="SanJose")
search_term = st.text_input("Enter a keyword (optional):")

limit = st.slider("Number of posts to analyze", min_value=1, max_value=20, value=5)

if st.button("Analyze"):
    with st.spinner("Fetching Reddit posts..."):
        try:
            posts = []
            if search_term:
                submissions = reddit.subreddit(subreddit_name).search(search_term, limit=limit)
            else:
                submissions = reddit.subreddit(subreddit_name).hot(limit=limit)

            for post in submissions:
                posts.append({"title": post.title, "selftext": post.selftext})

        except Exception as e:
            st.error(f"Failed to fetch posts: {e}")
            posts = []

    if posts:
        st.success("Fetched posts. Analyzing sentiment...")
        for idx, post in enumerate(posts, start=1):
            text_to_analyze = f"{post['title']} {post['selftext']}".strip()

            if not text_to_analyze:
                continue

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful sentiment analysis tool."},
                        {"role": "user", "content": f"Analyze the sentiment of this Reddit post: {text_to_analyze}"}
                    ]
                )

                sentiment = response.choices[0].message.content
                st.markdown(f"**Post #{idx}:** {post['title']}")
                st.markdown(f"*Sentiment:* {sentiment}")
                st.divider()

            except Exception as e:
                st.warning(f"OpenAI error for post #{idx}: {e}")
