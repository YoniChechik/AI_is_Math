def PPTtoPDF(inputFileName, outputFileName, formatType=32):
    try:
        import win32com.client

        app = win32com.client.Dispatch("PowerPoint.Application")
        ppt = app.Presentations.Open(inputFileName, ReadOnly=False)
        ppt.SaveAs(outputFileName, 32)  # formatType = 32 for ppt to pdf
        app.Quit()
        ppt = None
        app = None
    except:  # noqa
        import comtypes.client
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")

        # Set visibility to minimize
        powerpoint.Visible = 1
        # Open the powerpoint slides
        slides = powerpoint.Presentations.Open(inputFileName)
        # Save as PDF (formatType = 32)
        slides.SaveAs(outputFileName, 32)
        # Close the slide deck
        slides.Close()


if __name__ == '__main__':
    PPTtoPDF(r"C:\Users\jonathanch\Google Drive\cv course\slides\Edges.pptx",
             r"C:\Users\jonathanch\Google Drive\cv course\slides\test.pdf")
