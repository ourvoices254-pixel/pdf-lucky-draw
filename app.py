import random
import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="PDF Lucky Draw Picker", page_icon="🎉", layout="centered")

st.title("🎉 PDF Lucky Draw Winner Picker")
st.write("Upload a PDF containing your list of participants, and let the app pick a winner at random!")

# File uploader
uploaded_file = st.file_uploader("Upload Participant List (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Read PDF and extract text
    try:
        reader = PdfReader(uploaded_file)
        participants = []
        
        for page in reader.pages:
            text = page.extract_text()
            if text:
                # Split text into lines and clean up whitespace
                lines = text.split("\n")
                for line in lines:
                    cleaned_line = line.strip()
                    if cleaned_line:  # Ignore empty lines
                        participants.append(cleaned_line)
        
        # Remove duplicates if desired, or keep as is
        participants = list(dict.fromkeys(participants))
        
        st.success(f"Successfully loaded **{len(participants)}** participants!")
        
        # Preview participants in an expandable box
        with st.expander("View Participant List"):
            st.write(participants)
            
        # Pick winner button
        if participants:
            st.divider()
            if st.button("🎲 Pick a Winner!", type="primary", use_container_width=True):
                with st.spinner("Drumroll please... 🥁"):
                    winner = random.choice(participants)
                
                st.balloons()
                st.markdown(f"""
                ### 🏆 And the winner is...
                # **{winner}**! 🎊
                """)
        else:
            st.warning("No text could be extracted from this PDF. Please check the file formatting.")

    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")
