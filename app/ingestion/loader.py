import tempfile

from langchain_community.document_loaders import (
    PyPDFLoader
)


def load_pdf(uploaded_file):

    # CREATE TEMP FILE
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(
            uploaded_file.read()
        )

        temp_path = tmp_file.name

    # LOAD PDF
    loader = PyPDFLoader(
        temp_path
    )

    documents = loader.load()

    # EXTRACT TEXT
    full_text = ""

    for doc in documents:

        full_text += (
            doc.page_content + "\n"
        )

    return full_text