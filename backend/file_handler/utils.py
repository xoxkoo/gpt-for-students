from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def summarizeFile(filePath):
    query = """
            I have an exam tomorrow, and I need to summarize given context to prepare efficiently. 
            This given context contains important information related to my exam. 
            Considering the urgency, I'd like you to help me generate a concise summary that covers the key points. 
            Please ensure the summary is within a limit of 10% of the original content, rounded up. 
            Your assistance in providing a focused and comprehensive summary would be greatly appreciated. 
            Please highlight important facts of the context, use italics for citations, bold for headers, code blocks, unordered and ordered lists, and ensure the summary is concise. Be creative in presenting the information.
            Format the response in html language, dont include css styles, make sure to use the correct tags: 
            The bold text tag <b>
            The italic text tag <i>
            The heading tags <h1> to <h6>
            The link tag <a> - dont use this one
            The item tag <li>
            The ordered list tag <ol>
            The unordered list tag <ul>
            The section tag <div> - dont use this one
            The container tag <span> - dont use this one
            The bitmap image tag <img> - dont use this one
            The vector-based graphics tag <svg> - dont use this one
            The inline frame tag <iframe> - dont use this one
            The table tag <table>. - dont use this one
            Also exclude the tag <para>
            """

    # TODO: create a pdf from the response
    return query_file(filePath, query)


def query_file(filePath, query):
    loader = PyPDFLoader(filePath)
    pages = loader.load_and_split()

    embeddings = OpenAIEmbeddings()
    VectorStore = FAISS.from_documents(pages, embedding=embeddings)

    docs = VectorStore.similarity_search(query=query, k=3)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    chain = load_qa_chain(llm=llm, chain_type="stuff")

    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=query)

    print(f"response: {response}")
    return response


def generatePdf(context):
    from io import BytesIO
    from html.parser import HTMLParser
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        ListFlowable,
        ListItem,
    )

    # Create the PDF
    buffer = BytesIO()

    # Set up document styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading1"]
    body_style = styles["BodyText"]

    elements = []

    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.current_style = body_style
            self.buffer = []
            self.list_items = []
            self.link_href = None

        def handle_starttag(self, tag, attrs):
            if tag == "ul" or tag == "ol":
                self.list_items = []
            elif tag == "li":
                self.current_style = body_style
                self.buffer = []
            elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                self.current_style = heading_style
            elif tag == "p":
                self.current_style = body_style
            elif tag == "b":
                self.current_style = body_style.clone("Bold")
            elif tag == "i":
                self.current_style = body_style.clone("Italic")

        def handle_endtag(self, tag):
            if tag == "ul" or tag == "ol":
                elements.append(ListFlowable(self.list_items))
                self.list_items = []
            elif tag == "li":
                self.list_items.append(
                    ListItem(Paragraph("".join(self.buffer), self.current_style))
                )
            elif tag in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "b", "i", "a"]:
                elements.append(Paragraph("".join(self.buffer), self.current_style))

        def handle_data(self, data):
            cleaned_data = " ".join(data.split())
            self.buffer.append(cleaned_data)

    parser = MyHTMLParser()
    parser.feed(context)
    parser.close()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    doc.build(elements)

    buffer.seek(0)
    return buffer
