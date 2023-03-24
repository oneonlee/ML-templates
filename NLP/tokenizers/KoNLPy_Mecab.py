import re
from konlpy.tag import Mecab 
mecab = Mecab()

def tokenizer(text):

    # Use for cleansing
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)
    
    return mecab.morphs(text)


# As of January 31, 2023
# https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0
josa_list = ["JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JC", "JX"]
def josaless_tokenizer(text, josa_list):

    # Use for cleansing
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)
    
    pos_list = mecab.pos(text)

    token_list = []
    for (token, pos) in pos_list:
        if pos not in josa_list:
            token_list.append(token)
    
    return token_list


# As of January 31, 2023
# https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0
essential_list = ["NNG", "NNBC", "NNB", "NR", "NP", "NNP",
                "VV", "VV+EC", "VV+ETM", "VA",
                "SL", "SN", 
                "XSN",
                "MAG", "MM"]
def essential_tokenizer(text, essential_list):
    
    # Use for cleansing
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)
    
    pos_list = mecab.pos(text)
    
    token_list = []
    for (token, pos) in pos_list:
        if pos in essential_list:
            token_list.append(token)
    
    return token_list


def noun_tokenizer(text):
    
    # Use for cleansing
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)
    
    return mecab.nouns(text)


if __name__=="__main__":
    text = "와 이거 실화냐? 진짜 가슴이 웅장해진다 내가 생각했던 그 나투로와 사스케가 맞냐? 정말 세계관 최강자들의 싸움이다"
    print(f"Original Text: {text}")
    print(f"Tokenized Text: {tokenizer(text)}")
    print(f"Tokenized except Josa: {josaless_tokenizer(text, josa_list)}")
    print(f"Tokenized essential POS: {essential_tokenizer(text, essential_list)}")
    print(f"Tokenized only Nouns: {noun_tokenizer(text)}")
    
    """
    Original Text: 와 이거 실화냐? 진짜 가슴이 웅장해진다 내가 생각했던 그 나투로와 사스케가 맞냐? 정말 세계관 최강자들의 싸움이다
    Tokenized Text: ['와', '이거', '실화', '냐', '진짜', '가슴', '이', '웅장', '해진다', '내', '가', '생각', '했', '던', '그', '나투', '로', '와', '사스케', '가', '맞', '냐', '정말', '세계관', '최강', '자', '들', '의', '싸움', '이', '다']
    Tokenized except Josa: ['와', '이거', '실화', '냐', '진짜', '가슴', '웅장', '해진다', '내', '생각', '했', '던', '그', '나투', '사스케', '맞', '냐', '정말', '세계관', '최강', '자', '들', '싸움', '이', '다']
    Tokenized essential POS: ['이거', '실화', '진짜', '가슴', '내', '생각', '그', '나투', '사스케', '맞', '정말', '세계관', '최강', '자', '들', '싸움']
    Tokenized only Nouns: ['이거', '실화', '가슴', '내', '생각', '나투', '사스케', '세계관', '최강', '싸움']
    """
