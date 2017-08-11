def read_text():
   quotes = open("D:\quotes.txt")
   contents_of_file=quotes.read()
   print(contents_of_file)
   quotes.close()
read_text()    
