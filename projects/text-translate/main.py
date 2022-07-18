# Download the required library 
# pip install translate 

from translate import Translator
translator= Translator(to_lang="zh")
translation = translator.translate("This is a pen.")