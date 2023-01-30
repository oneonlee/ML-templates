import fasttext

def tokenizer(text):
  
    # Use for cleansing
    # text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)

    return fasttext.FastText.tokenize(text)
