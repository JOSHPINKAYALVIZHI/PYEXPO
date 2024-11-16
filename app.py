
import streamlit as st
import random

def web_portalfolio():
    # Page configs
    st.set_page_config(page_title="Joshpin Kayalvizhi's Portfolio", page_icon="🌟")
    st.markdown("""
        <style>
        div.block-container {
            padding-top: 2rem;
            margin-top: 2rem;
            margin-left: 3rem; /* Adjust as needed */
            margin-right: 3rem; /* Adjust as needed */
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with your name
    st.write(f"""
        <div class="title" style="text-align: center;">
        <span style='font-size:32px;'>Hello! My name is Joshpin Kayalvizhi</span>🖐🏻
        </div>
    """, unsafe_allow_html=True)

    # Adjusting padding for better layout
    st.markdown('<style>div.block-container{padding-top:2rem;}<style>', unsafe_allow_html=True)

    # Short introduction about yourself
    st.markdown("""
        I am deeply interested in the field of artificial intelligence, where technology can work with 
        human ideas to solve tough problems. My goal is to become an AI Engineer, as I believe AI has the power to change 
        industries, improve lives, and help us learn new things. I love the mix of math, coding, and data work involved in
        building intelligent systems that can learn and adapt on their own. I’m excited to keep growing my skills and want 
        to use them to create helpful solutions that make a positive impact on the world.
    """)

    # Sidebar navigation
    selected = st.sidebar.radio(
        "Select a Section", ["Education", "Contact", "Guessing Game"]
    )

    # Education Section
    if selected == "Education":
        with st.container():
            st.subheader("1 Year AI & Data Science Program")
            st.title("KGISL Institute Of Technology, Saravanampatti")
            st.write("""
                The 1-Year BTech in AI and Data Science at KGISL Institute of Technology is a specialized program 
                designed for students passionate about artificial intelligence and data science. The course covers 
                essential topics such as machine learning, deep learning, data analytics, and programming skills 
                in Python. Students also gain hands-on experience with tools like TensorFlow, PyTorch, and Pandas.

                **Core Topics Covered:**
                - Machine Learning: Supervised and Unsupervised Learning
                - Deep Learning: Neural Networks, CNNs, RNNs
                - Data Analysis and Visualization
                - Artificial Intelligence Applications

                This program prepares students to work on real-world AI problems and to advance their careers in 
                data science and AI engineering.
            """)
            st.write("___")

    # Contact Section
    elif selected == "Contact":
        with st.container():
            st.subheader("Get in Touch")
            st.write("""
                If you have any questions about my work or would like to get in touch with me, feel free to reach out!
            """)

            st.write("**KGISL Institute of Technology**")
            st.write("Saravanampatti, Coimbatore")
            st.write("Phone: +91-123-456-7890")
            st.write("Email: info@kgisltech.ac.in")
            st.write("___")

    # Guessing Game Section
    elif selected == "Guessing Game":
        with st.container():
            st.subheader("Number Guessing Game")
            st.write("___")

            # Game setup
            target_number=5
            if 'target_number' not in st.session_state:

                st.session_state.attempts = 0

            # Input for user's guess
            guessed_number = st.number_input("Enter your guess from 1 to 10:")
            if st.button("Check Guess"):
                st.session_state.attempts += 1
                if guessed_number < target_number:
                    st.warning("Try a higher number!")
                elif guessed_number > target_number:
                    st.warning("Try a lower number!")
                else:
                    st.success(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
                    # Reset the game

                    st.session_state.attempts = 0

            st.write("___")
            st.write("To reset the game, reload the page or keep guessing until you succeed.")

if __name__ == "__main__":
    web_portalfolio()
