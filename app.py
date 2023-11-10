## will need to pip install pipeline and tensorflow
## this code comes from: https://www.kdnuggets.com/2021/10/simple-question-answering-web-app-hugging-face-pipelines.html

import streamlit as st
from transformers import pipeline

def load_file():
    """Load text from file"""
    uploaded_file = st.file_uploader("Upload Files",type=['txt'])

    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            raw_text = str(uploaded_file.read(),"utf-8")
        return raw_text


if __name__ == "__main__":

    # App title and description
    st.title("Answering questions from text")
    st.write("Upload text, pose questions, get answers")

    # Load file
    raw_text = load_file()
    if raw_text != None and raw_text != '':

        # Display text
        with st.expander("See text"):
            st.write(raw_text)

        # Perform question answering
        question_answerer = pipeline('question-answering')

        answer = ''
        question = st.text_input('Ask a question')

        if question != '' and raw_text != '':
            answer = question_answerer({
                'question': question,
                'context': raw_text
            })

        # st.write(answer)
        def extract_context(raw_text, start, end, additional_chars=10):
            
            # Calculate the start and end indices with additional context
            start_context = max(0, start - additional_chars)
            end_context = min(len(raw_text), end + additional_chars)

            # Extract the section with additional context
            return raw_text[start_context:end_context]

        # Example usage
        start = 600  # start index from QA output
        end = 611    # end index from QA output

        # Assume raw_text is your text data
        # raw_text = "Your full text data here..."

        extracted_text = extract_context(raw_text, start, end)

        # Use Streamlit to write the extracted text
        st.write(extracted_text)
