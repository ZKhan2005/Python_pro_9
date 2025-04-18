import streamlit as st

# Page config for dark, futuristic feel
st.set_page_config(
    page_title="FitVerse",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for futuristic neon style
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
        }
        .main {
            background-color: #111;
            color: #00f0ff;
        }
        h1, h2, h3 {
            color: #00ffe5;
        }
        .stButton>button {
            background-color: #00f0ff;
            color: black;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔹 FitVerse Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ About", "📞 Contact"])

# Home Page
if page == "🏠 Home":
    st.title("💪 Welcome to FitVerse")
    st.subheader("Your futuristic hub for Fitness & Health")

    st.image("https://images.unsplash.com/photo-1605296867304-46d5465a13f1", use_column_width=True)

    st.markdown("""
    - 🏋️ Personalized workouts  
    - 🥗 Nutrition guidance  
    - 📈 Progress tracking  
    - 🌐 Accessible anytime, anywhere
    """)

# About Page
elif page == "ℹ️ About":
    st.title("🌟 About FitVerse")
    st.image("https://images.unsplash.com/photo-1584467735871-39d236250c1d", width=600)
    st.write("""
    FitVerse is your go-to platform for all things health and fitness.
    Our mission is to help you live stronger, healthier, and happier.
    
    **Why FitVerse?**
    - Modern tools with futuristic design
    - AI-powered fitness recommendations
    - Real-time tracking and analytics
    """)

# Contact Page
elif page == "📞 Contact":
    st.title("📬 Get in Touch")
    st.image("https://images.unsplash.com/photo-1581092580492-cc8cf3d2f6dd", width=600)
    st.markdown("""
    **Email:** support@fitverse.ai  
    **Phone:** +1-800-FIT-VERSE  
    **Address:** 101 Galaxy Gym Street, Neon City
    """)

    st.subheader("📤 Send us a message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send"):
        st.success("✅ Your message has been sent!")
