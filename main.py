import streamlit as st
import requests

def get_random_joke():
    """Fetch random joke from the (API)"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:  # Fixed: reversed -> response
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "An error occurred while fetching the joke. Please try again later."
    except Exception as e:
        return "Why do programmers prefer dark mode? 👉 Because the light attracts bugs! 🐛💻😂 "
    
def main():
    st.title("Random Joke Generator😜")
    # Moved markdown inside main()
    st.markdown("""## Life is too short for bad vibes—let's add some laughter! 😂
    A smile is the best outfit you can wear, and laughter is the best medicine! 😂✨
    Why take life too seriously when a good joke can turn your day around? 😆🔥
    Get ready to laugh out loud—because happiness starts here! 🚀💜
    """)

    if st.button("Generate Joke😁"):
        joke = get_random_joke()
        st.info(joke)

if __name__ == "__main__":
    main()

