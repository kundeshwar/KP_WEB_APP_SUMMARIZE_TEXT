#------------------------------------------Import useful labrary 
import streamlit as st #for web app 
from txtai.pipeline import Summary #for summarize text 
from PyPDF2 import PdfReader # to read pdf file 
from streamlit_lottie import st_lottie
import requests
#-------------------------------------set page config 
st.set_page_config(page_title="KP APP", page_icon=":sunglasses:", layout="wide", initial_sidebar_state="expanded")
#-----------------------------use lottie here 
def lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
loettie_1 = lottie("https://assets10.lottiefiles.com/packages/lf20_gigyrcoy.json") 
loettie_2 = lottie("https://assets10.lottiefiles.com/packages/lf20_gigyrcoy.json")
#-----------------------------------creat function for text summary 
@st.cache_resource #it is for streamlit 
def text_summary(text, maxlength=None):
    #create summary instance
    summary = Summary() #import model 
    text = (text)
    result = summary(text) #add text into model 
    return result 
#--------------------------------creat function to read document 
def extract_text_from_pdf(file_path):
    # Open the PDF file using PyPDF2
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text
#-----------------------------------------creat sidebar
option = "KP 😎 APP" 
st.sidebar.markdown(f"<h1 style='text-align: center;'>{option}</h1>",unsafe_allow_html=True)
st.sidebar.markdown("-----------------")
st.sidebar.markdown("")
choice = st.sidebar.selectbox("Select Your Option  :grinning: :-        ", ["Summarize Text", "Summarize Document"])

#-----------------------------------------For text summary
#first write for summarize text 
if choice == "Summarize Text":
    #header 
    #st.header("KP :heartbeat: App To Summarize Text :stuck_out_tongue_winking_eye: ")
    option = "KP 💓 App To Summarize Text 😜 "
    st.markdown(f"<h2 style='text-align: center;'>{option}</h2>",unsafe_allow_html=True)
    st.markdown("-----------------")
    st.markdown("")
    #input box 
    input_text = st.text_area("Paste Your Text Here")
    #input none condition
    if input_text is not None: 
        button_1 = st.button("Summarize Text")
        #button press condition 
        if button_1:
        
            #divide page into two columns 
            col1, col2 = st.columns([1, 1])
            #with first columns 
            with col1:
                #st.markdown(f"<h3 style='text-align: center;'> Your Input Text :sunglasses: </h3>",unsafe_allow_html=True)
                st.markdown("Your Input Text :sunglasses:")
                st.info(input_text)
            #print our result in second columns 
            with col2:
                result = text_summary(input_text)
                st.markdown("Summarize text :heart_eyes: ")
                st.info(result)
        st_lottie(loettie_1)
    
#-----------------------------------for text documnet 
elif choice == "Summarize Document":
    #st.subheader("Summarize Document using txtai")
    #st.header("KP :heartbeat: App To Summarize Document :stuck_out_tongue_winking_eye: ")
    option = "KP 💓 App To Summarize Document 😜 "
    st.markdown(f"<h2 style='text-align: center;'>{option}</h2>",unsafe_allow_html=True)
    st.markdown("-----------------")
    st.markdown("")
    #file_uploder 
    input_doc =  st.file_uploader("Upload Your Document", type=["pdf"], accept_multiple_files=False, label_visibility="visible")
    #condition for none file 
    if input_doc is not None:
        #condition for none button
        button_2 = st.button("Summarize Document")
        if button_2:
            #save that file into our system 
            with open("doc_file.pdf", "wb") as f:
                f.write(input_doc.getbuffer())
                #divide that page into columns 
            col1, col2 = st.columns([1,1])
            #first col
            with col1:
                #print the msg for file upload 
                st.info("File uploaded successfully")
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("Input File Text :sunglasses: ")
                #print our file text 
                st.info(extracted_text)
            with col2:
                #print our summary text by using summary text function 
                st.markdown("Summarize text :heart_eyes: ")
                text = extract_text_from_pdf("doc_file.pdf")
                doc_summary = text_summary(text)
                st.success(doc_summary)
    st_lottie(loettie_2) 
                