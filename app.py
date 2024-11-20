import streamlit as st
import cohere

# Initialize Cohere client
api_key = "3O2uRDDVta5S6yDmaYBCeEjVHc3ZAch6j7olGy9H"  # Replace with your actual Cohere API key
co = cohere.Client(api_key)

# Function to generate story from prompt
def generate_story(prompt):
    try:
        # Try using a different model like "command-light"
        response = co.generate(
            model="command-light",  # Change this model if necessary
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.generations[0].text
    except cohere.errors.NotFoundError as e:
        return f"Error: {e}"

# Streamlit App Layout
st.title("Text-to-Story Generator")
st.markdown("Enter a text prompt below to generate a story:")

# User input for the prompt
user_input = st.text_area("Enter your text prompt:")

# Button to generate story
if st.button("Generate Story"):
    if user_input:
        # Generate the story based on user input
        story = generate_story(user_input)
        st.subheader("Generated Story:")
        st.write(story)
    else:
        st.write("Please enter a prompt to generate a story.")