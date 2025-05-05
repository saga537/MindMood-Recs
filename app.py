import streamlit as st
from utils import detect_theme
from recommender import get_movie_recommendations, get_book_recommendations

st.set_page_config(page_title="MindMood Recs", layout="centered")
st.write("✅ App loaded successfully!")

st.title("🎯 MindMood Recs")
st.write("Tell us what you're thinking or feeling. We'll recommend books or movies that match your mood.")

user_input = st.text_area("What's on your mind?", height=150)

if st.button("Get Recommendations"):
    if not user_input.strip():
        st.warning("Please enter something first.")
    else:
        with st.spinner("Analyzing your thoughts..."):
            theme = detect_theme(user_input)
            st.success(f"We detected your theme: **{theme}**")

            # Uncommented movie recommendations
            movies = get_movie_recommendations(theme)  # If this is working fine, use it.
            books = get_book_recommendations(theme)

            # Movie Recommendations
            st.subheader("🎬 Movie Recommendations")
            if not movies:
                st.write("No matching movies found.")
            for movie in movies:
                st.markdown(f"**{movie['title']}**")
                st.write(movie.get('overview', 'No description available.'))

            # Book Recommendations
            st.subheader("📚 Book Recommendations")
            if not books:
                st.write("No matching books found.")
            for book in books:
                info = book.get('volumeInfo', {})
                st.markdown(f"**{info.get('title', 'Unknown Title')}**")
                st.write(info.get('description','No description available.'))  




