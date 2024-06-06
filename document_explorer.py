from docx import Document

def extract_headings_and_contents(doc_path):
    doc = Document(doc_path)
    headings_and_contents = {}
    current_heading = None
    current_content = []

    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('Heading'):
            # New heading found, store previous heading and content
            if current_heading is not None:
                headings_and_contents[current_heading] = '\n'.join(current_content)
            # Update current heading and reset content
            current_heading = paragraph.text
            current_content = []
        else:
            # Add paragraph to current content
            current_content.append(paragraph.text)

    # Add last heading and content
    if current_heading is not None:
        headings_and_contents[current_heading] = '\n'.join(current_content)

    return headings_and_contents
