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


# As of March 24, 2023
# https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0
essential_list = ["NNG", "NNBC", "NNB", "NR", "NP", "NNP", # 명사 종류들
                  "VV", "VV+EC", "VV+ETM", "VA", # 동사 및 형용사 종류들
                  "SL", "SN", # SL: 외국어, SN: 숫자
                  "XSN", # 명사파생 접미사
                  "MAG", "MM" # MM: 관형사, MAG: 일반 부사
                 ]
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
    
    
    text = "XX 년 8 월 0000 편 제주에서 김포로 가기 위하여 00:00 분경 FL250 에 도달하여 순항 중 광주북쪽지역에 심한 thunderstorm 이 발생하여 인천 control 에 우측으로 10NM deviation request 하였음."
    print(f"Original Text: {text}")
    print(f"Tokenized Text: {tokenizer(text)}")
    print(f"Tokenized except Josa: {josaless_tokenizer(text, josa_list)}")
    print(f"Tokenized essential POS: {essential_tokenizer(text, essential_list)}")
    print(f"Tokenized only Nouns: {noun_tokenizer(text)}")
    
    """
    Original Text: XX 년 8 월 0000 편 제주에서 김포로 가기 위하여 00:00 분경 FL250 에 도달하여 순항 중 광주북쪽지역에 심한 thunderstorm 이 발생하여 인천 control 에 우측으로 10NM deviation request 하였음.
    Tokenized Text: ['XX', '년', '8', '월', '0000', '편', '제주', '에서', '김포', '로', '가', '기', '위하', '여', '0000', '분경', 'FL', '250', '에', '도달', '하', '여', '순항', '중', '광주', '북쪽', '지역', '에', '심한', 'thunderstorm', '이', '발생', '하', '여', '인천', 'control', '에', '우측', '으로', '10', 'NM', 'deviation', 'request', '하', '였', '음']
    Tokenized except Josa: ['XX', '년', '8', '월', '0000', '편', '제주', '김포', '가', '기', '위하', '여', '0000', '분경', 'FL', '250', '도달', '하', '여', '순항', '중', '광주', '북쪽', '지역', '심한', 'thunderstorm', '발생', '하', '여', '인천', 'control', '우측', '10', 'NM', 'deviation', 'request', '하', '였', '음']
    Tokenized essential POS: ['XX', '년', '8', '월', '0000', '편', '제주', '김포', '가', '위하', '0000', '분경', 'FL', '250', '도달', '순항', '중', '광주', '북쪽', '지역', 'thunderstorm', '발생', '인천', 'control', '우측', '10', 'NM', 'deviation', 'request']
    Tokenized only Nouns: ['년', '월', '편', '제주', '김포', '분경', '도달', '순항', '중', '광주', '북쪽', '지역', '발생', '인천', '우측']
    """
