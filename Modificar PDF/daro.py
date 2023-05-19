import aspose.words as aw
 

doc = aw.Document("c:\\Users\DA RO\Desktop\Pythonpdf\Pdf\pdfuser.pdf")
 
builder = aw.DocumentBuilder(doc)

# Insertar texto al principio del documento.
builder.move_to_document_start()
#builder.writeln("Morbi enim nunc faucibus a.")
#builder.Image.FromFile(docimagen)

#Imagen por URL
#builder.insert_image("https://w7.pngwing.com/pngs/554/416/png-transparent-goku-gohan-frieza-dragon-ball-z-legendary-super-warriors-goten-goku-superhero-fictional-character-cartoon.png");

#Imagen Local
#builder.insert_image("./Radicado/radicado.png")

##Imagen local con posicion
builder.insert_image("./Radicado/radicado.png",
                      aw.drawing.RelativeHorizontalPosition.MARGIN, 100,
    aw.drawing.RelativeVerticalPosition.MARGIN, 100, 200, 100, aw.drawing.WrapType.SQUARE)


doc.update_page_layout()

doc.save("Output.pdf")





