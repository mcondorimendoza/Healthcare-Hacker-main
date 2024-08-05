import streamlit as st


# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6f9;
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        background-color: #007acc;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .main-header h1 {
        color: white;
    }
    .module-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    .module {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        margin: 10px;
        text-align: center;
        flex: 1 1 200px;
        max-width: 200px;
    }
    .module img {
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        width: 100%;
        height: 150px;
        object-fit: cover;
    }
    .module button {
        background-color: #007acc;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 0 0 10px 10px;
        width: 100%;
        cursor: pointer;
        font-weight: bold;
    }
    .module button:hover {
        background-color: #005fa3;
    }
    .content-container {
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        position: relative;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Custom header
st.markdown('''
    <div class="main-header">
        <h1>Healthcare Assistant</h1>
    </div>
''', unsafe_allow_html=True)

# Load images
symptom_tracker_image = "D:/falcon-healthcare/images/symptom_tracker.jpg"
medical_image_analysis_image = "images/medical_image_analysis.jpg"
reports_visualizations_image = "images/reports_visualizations.jpg"
medical_chatbot_image = "images/medical_chatbot.jpg"

# Initialize session state for navigation
if "active_section" not in st.session_state:
    st.session_state.active_section = "Home"

# Image click handling
def set_active_section(section):
    st.session_state.active_section = section

# Display module options
if st.session_state.active_section == "Home":
    st.markdown('<div class="module-container">', unsafe_allow_html=True)
    
    st.markdown(f'''
        <div class="module">
            <img src="{symptom_tracker_image}" alt="Symptom Tracker">
            <button onclick="window.location.href='/Symptom Tracker'">Symptom Tracker</button>
        </div>
        <div class="module">
            <img src="{medical_image_analysis_image}" alt="Medical Image Analysis">
            <button onclick="window.location.href='/Medical Image Analysis'">Medical Image Analysis</button>
        </div>
        <div class="module">
            <img src="{reports_visualizations_image}" alt="Reports & Visualizations">
            <button onclick="window.location.href='/Reports & Visualizations'">Reports & Visualizations</button>
        </div>
        <div class="module">
            <img src="{medical_chatbot_image}" alt="Medical Chatbot">
            <button onclick="window.location.href='/Medical Chatbot'">Medical Chatbot</button>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Display content based on active section
else:
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    if st.session_state.active_section == "Symptom Tracker":
        st.header("Symptom Tracker")
        st.write("Track your symptoms here.")
        
        # Additional Row for Pain Level and Other Symptoms
        st.markdown('<h3>Pain Level</h3>', unsafe_allow_html=True)
        pain_level = st.slider("Pain Level (0-10)", 0, 10, 0)
        st.write(f"Pain Level: {pain_level}")

    elif st.session_state.active_section == "Medical Image Analysis":
        st.header("Medical Image Analysis")
        st.write("Analyze medical images here.")
        # Add your medical image analysis implementation here

    elif st.session_state.active_section == "Reports & Visualizations":
        st.header("Reports & Visualizations")
        st.write("View reports and visualizations here.")
        # Add your reports and visualizations implementation here

    elif st.session_state.active_section == "Medical Chatbot":
        st.header("Medical Chatbot")

        # Function to get response from the medical assistant API
        def get_response(prompt):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "medical-assistant-model",
                "messages": [
                    {"role": "system", "content": "You are a medical assistant. Provide clear and accurate medical responses based on the symptoms described."},
                    {"role": "user", "content": prompt}
                ]
            }
            try:
                response = requests.post(API_URL, headers=headers, json=data)
                response.raise_for_status()
                response_json = response.json()
                return response_json.get('choices', [{}])[0].get('message', {}).get('content', "No response received.")
            except RequestException as e:
                st.error(f"An error occurred: {e}")
                return "Sorry, there was an error processing your request."

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            css_class = "user" if role == "user" else "assistant"
            st.markdown(f'<div class="chat-message {css_class}"><strong>{role.capitalize()}</strong>: {content}</div>', unsafe_allow_html=True)

        # Accept user input
        if prompt := st.text_input("What is your medical concern?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            st.markdown(f'<div class="chat-message user"><strong>User</strong>: {prompt}</div>', unsafe_allow_html=True)

            # Get response from the medical assistant API
            response = get_response(prompt)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            # Display assistant response in chat message container
            st.markdown(f'<div class="chat-message assistant"><strong>Assistant</strong>: {response}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Custom footer
st.markdown("""
    <div style="background-color: #007acc; color: white; padding: 10px; border-radius: 10px; text-align: center; margin-top: 20px;">
        <p>Healthcare Assistant © 2024</p>
    </div>
""", unsafe_allow_html=True)
