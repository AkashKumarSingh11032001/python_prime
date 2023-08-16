from importsPackage import gTTS,PyPDF2, getFileNameFromFilePath

def pdfToAudio(filePath):
    pdf_File = open(filePath, 'rb') 


    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    count = pdf_Reader.numPages # counts number of pages in pdf
    textList = []

    #Extracting text data from each page of the pdf file
    for i in range(count):
       try:
        page = pdf_Reader.getPage(i)    
        textList.append(page.extractText())
       except:
           return False

    #Converting multiline text to single line text
    textString = " ".join(textList)
    language = 'en'
    myAudio = gTTS(text=textString, lang=language, slow=False)
    
    file_name = getFileNameFromFilePath(filePath)+".mp3"
    myAudio.save(file_name)
    
    return True