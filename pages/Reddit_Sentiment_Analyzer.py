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

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎 • Powered by OpenAI & Streamlit")

#------------------------------------------------------------------------------------------------------------------------------------------------------

# chatbot on the side
st.sidebar.title("💬 HelpBot")
st.sidebar.write("Need help with Emergency Interim Housing (EIH)? Ask anything.")

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# user input area
user_input = st.sidebar.text_input("You:", key="user_input", placeholder="e.g., Can I apply for shelter if I have a pet?")

# If user submits a message
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(("You", user_input))

    # Generate AI response using OpenAI
    with st.spinner("Thinking..."):
        try:
            messages = [{"role": "system", "content": "You are a helpful assistant that specializes in Emergency Interim Housing (EIH) in San Jose and Santa Clara County. Be concise, helpful, and clear."}]
            
            # Add all previous messages to maintain context
            for sender, message in st.session_state.chat_history:
                role = "user" if sender == "You" else "assistant"
                messages.append({"role": role, "content": message})

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.6,
                max_tokens=500
            )

            bot_reply = response.choices[0].message.content.strip()
            st.session_state.chat_history.append(("Bot", bot_reply))

        except Exception as e:
            bot_reply = "⚠️ Sorry, I ran into an error. Please try again."
            st.session_state.chat_history.append(("Bot", bot_reply))
            st.error(f"Error: {e}")