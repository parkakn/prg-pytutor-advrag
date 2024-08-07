# Packages we need: 
from llama_parse import LlamaParse

class documentparser:    
    
    # Want: PDF -> Markdown
    # Input: 
    # Document file paths (doc), Type of Document (doc_type)

    # Parser function
    def document_to_markdown(doc,doc_type):
        # Determine type of documnet 
        # Parsing Instructions 
        if doc_type == "lab manual":
            # Lab Manual
            parsingInstruction = """
            The provided document is lab manual with step-by-step guides. 
            It contains embedded images to help with understanding the process to complete the task. 
            Extract the text and structure of the contents in these files. 
            Extract embedded images and provide a description for them in as much detail as possible. 
            Make sure to extract embedded images as well as have a reference to it in the correct location of the documnet. 
            """
        elif doc_type == "assignment":
            # Assignments
            parsingInstruction = """
            The provided document is an assignment for students to complete for an introduction to programming course. 
            IMPORTANT: Tasks or contents might be related across pages, so make sure you capture the relevant content across consecutive pages. 
            It lists the specific tasks and the desired objectives to be met through the tasks.
            Extract the structure and text of the document as well as any embedded objects.
            """
        elif doc_type == "in-class exercise":
            # In-class exercises
            parsingInstruction = """
            The provided document contains exercise questions either as multiple choice or short answer questions. 
            It may ask to describe a given image. Extract and give a reference to this embedded image. 
            Extract the text and structure of these documents. 
            """

        elif doc_type == "lecture slide":
            # Lecture slides
            parsingInstruction = """
            The provided document is a lecture slide for a course on introductory programming and computer science. 
            Convert the provided document content into markdown file format. 
            Note that there are embedded figures, bullet points, code snippets, flowcharts, etc. 
            Infer what each page is trying convey and summarize the contents.
            If you encounter a flowchart or an image, give a summary or explanation of it while also extracting text and structure of it. If possible, also related to the concept being conveyed or discussed.  
            Also, try to extract the structure, hierarchy, and formatting of the contents where texts exist.
            """

        # Set up parser: Multi-modal LLM using LlamaIndex's LlamaParse 
        parser_gpt4o = LlamaParse(
                            result_type="markdown",
                            parsing_instruction=parsingInstruction,
                            use_vendor_multimodal_model=True,
                            vendor_multimodal_model="openai-gpt4o",
                            invalidate_cache = True
                        )

        # Initiate parsing and store in a list 
        documents = [] 
        for pdf_file in doc:
            # Generate a unique name for each .pkl file based on the PDF file name
            #pkl_filename = os.path.basename(pdf_file).replace('.pdf', '.pkl')
            #pkl_filepath = os.path.join("GSU - CIS 3260 - Fall 2023/", pkl_filename)

            # Load and parse the data
            document = parser_gpt4o.load_data(pdf_file) 
            documents.append(document)

            # Save the parsed document to a .pkl file
            # with open(pkl_filepath, 'wb') as f:
            #     pickle.dump(document, f)
            # print(f"Saved parsed document to {pkl_filepath}")

        # return list of parsed documents 
        return documents 