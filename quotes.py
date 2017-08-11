import urllib
def read_text():
   quotes = open("D:\quotes.txt")
   contents_of_file=quotes.read()
   print(contents_of_file)
   quotes.close()
   check_profanity(contents_of_file)
def check_profanity(text_to_check):
   connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
   output=connection.read()
   
   if "true" in output:
      print("\nProfanity Alert!!!")
   elif "false" in output:
      print("\nNo curse words in the document")
   else:
      print("\nDocument format is not supported.please try again ")
      
   connection.close()


read_text()    
