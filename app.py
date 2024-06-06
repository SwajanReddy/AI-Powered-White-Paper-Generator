import streamlit as st
from io import BytesIO
from document_explorer import extract_headings_and_contents
from geminiAI import  run_bot


# Page title
st.title('Generate White Paper Summary Document')

# Upload file
uploaded_file = st.file_uploader("Upload your word document below", type=["docx"])
flag = 0


if uploaded_file is not None:
    # Display file details
    st.write("File uploaded:", uploaded_file.name)

    # Process the uploaded file (this is a placeholder for actual processing logic)
    if st.button("Process Document"):
        headings_and_contents = extract_headings_and_contents(uploaded_file)
        progress_text = st.empty()
        # Status variables
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        progress_text.write("Processing... estimated time to complete: 6 min")
        
        doc, flag = run_bot(headings_and_contents, progress_text, status_text, progress_bar)
        print(type(doc))
        st.session_state.doc = doc
        
    if flag: 
        progress_text.write("processing completed, hit download.")
        
    # Download button
    if st.button("Download Summary"):
        if 'doc' not in st.session_state:
            st.error("Please process the document first.")
        else:
            # Create a byte stream to hold the document
            doc_stream = BytesIO()
            st.session_state.doc.save(doc_stream)
            doc_stream.seek(0)
    
            # Download the document
            st.download_button(
                label="Download Document",
                data=doc_stream,
                file_name="summary.docx",
                mime="application/docx"
            )
