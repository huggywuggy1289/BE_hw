from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext'] #요청(request)가 들어오면 fulltext를 가져와라
    word_list = entered_text.split() #entered_text를 공백기준으로 문자열을 나누겠다.
    word_count = len(word_list)

    #글자 수 세기
    char_count = len(entered_text)

    # 띄어쓰기를 제외한 글자 수 세기 " "을 ""으로 replace하다.
    nospace_count = len(entered_text.replace(" ", ""))

    word_directory ={}

    for word in word_list:
        if word in word_directory:
            word_directory[word] +=1 #단어를 발견하면 그 단어의 출현횟수를 더해줘라
        else:
            word_directory[word] = 1 #아니라면 그냥 반환ㄱㄱ

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_directory.items(), 'word_count': word_count, 'char_count' : char_count, 'nospace_count':nospace_count})
# result.html에서 alltext문자열변수: entered_text를 적용시키고, 딕셔너리문자열변수: 단어 디렉터리를 받아온다.
# def result1(request):
#     entered_text = request.GET['fulltext']
#     word_list = entered_text.split()
#     word_count = len(word_list)

#     return render(request, 'result.html', {'alltext': entered_text, 'word_count': word_count})
