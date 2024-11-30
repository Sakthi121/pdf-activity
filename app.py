import PyPDF2
import streamlit as st

# Function to merge multiple PDFs
def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into a single PDF."""
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_files:
        merger.append(pdf)
    
    # Write the merged PDF to the output path
    merger.write(output_path)
    merger.close()

# Streamlit UI setup
st.title("Merge Multiple PDFs into One")

# File uploader for multiple PDF files
uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    # Display filenames of uploaded files
    st.write("Uploaded files:")
    file_names = [file.name for file in uploaded_files]
    st.write(file_names)

    # User selects the files in the desired order using a multiselect box
    reordered_files = st.multiselect(
        "Select PDFs to merge in order", file_names, default=file_names
    )

    # Button to start the merging process
    if st.button("Merge PDFs"):
        # Reorder the files based on user selection
        ordered_pdf_files = [uploaded_files[file_names.index(file_name)] for file_name in reordered_files]
        
        # Specify output path for merged PDF
        output_pdf = "merged_output.pdf"

        # Merge the PDFs
        merge_pdfs(ordered_pdf_files, output_pdf)

        # Provide download option for the merged PDF
        with open(output_pdf, "rb") as f:
            st.download_button(
                label="Download Merged PDF",
                data=f,
                file_name=output_pdf,
                mime="application/pdf"
            )
