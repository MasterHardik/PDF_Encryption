import pikepdf

old_pdf = pikepdf.Pdf.open("SamplePDF_EncryptionUsingPython.pdf")  #heree we need to change the name of the file and then that perticular file will only be targeted

no_extr = pikepdf.Permissions(extract =False)

old_pdf.save   ("Encrypted_pdf_created_using_python_pikepdf.pdf",
                encryption=pikepdf.Encryption(user="123asdf",  #this is going to be the pwd for your encrypted file
                                             owner="master",
                                             allow=no_extr))