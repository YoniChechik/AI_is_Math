import win32com.client

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    app = win32com.client.Dispatch("PowerPoint.Application")
    ppt = app.Presentations.Open(inputFileName, ReadOnly= False)
    ppt.SaveAs(outputFileName, 32) # formatType = 32 for ppt to pdf
    app.Quit()
    ppt =  None
    app = None


if __name__ == '__main__':
    PPTtoPDF(r"C:\Users\jonathanch\Google Drive\cv course\slides\Edges.pptx", r"C:\Users\jonathanch\Google Drive\cv course\slides\test.pdf")


