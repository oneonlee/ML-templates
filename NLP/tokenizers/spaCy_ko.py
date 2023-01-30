import spacy

get_ipython().system('python3 -m spacy download ko_core_news_sm')
# In the Jupyter, you can replace -> !python3 -m spacy download ko_core_news_sm
# Or enter the command on Cmd/Terminal.

spacy_ko = spacy.load('ko_core_news_sm')

def tokenizer(text):
  
    # Use for cleansing
    # text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)
    
    return [tok.text for tok in spacy_ko.tokenizer(text)]
