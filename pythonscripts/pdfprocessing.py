import PyPDF2
import sys

def ReadPdfContent():
    with open('documents/dummy.pdf','rb') as file:
        reader=PyPDF2.PdfFileReader(file)
        print(reader.numPages)
       
        page=reader.getPage(0)
        page.rotateClockwise(90)
        writer=PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('documents/dummy-rotate.pdf','wb') as new_file:
            writer.write(new_file)
            print('All done !!')

def MergePdfs():
    inputs=sys.argv[1:]
    merger=PyPDF2.PdfFileMerger()
    for pdf in inputs:
        print(pdf)
        merger.append(pdf) 
    
    merger.write('documents/combine.pdf')   
    print('All done !!')


def AddWaterMarkPdfs():
    template=PyPDF2.PdfFileReader(open('documents/combine.pdf','rb'))
    watermark=PyPDF2.PdfFileReader(open('documents/watermark.pdf','rb'))
    output=PyPDF2.PdfFileWriter();

    for number in range(template.getNumPages()):
        page=template.getPage(number)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('documents/watermark_combinepdf.pdf','wb') as file:
            output.write(file)
            print('All done !!')

#calling methods

#ReadPdfContent();

#MergePdfs()

AddWaterMarkPdfs()