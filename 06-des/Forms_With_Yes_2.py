import string


def Formatting(link):
    with open(link) as f:
        txt = f.read().split("\n\n")
    txt = [i.split("\n") for i in txt]
    return txt


def FindCommonAnswers(Answers: list):
    CommonAnswers = set([i for i in string.ascii_lowercase])
    for i in Answers:
        CommonAnswers = CommonAnswers.intersection(set(i))

    return CommonAnswers


def FindCount(AnswersList):
    count = 0
    for i in AnswersList:
        count += len(FindCommonAnswers(i))

    print(count)


link = (
    "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\06-des\\Form_Answers.txt"
)

AnswersList = Formatting(link)

FindCount(AnswersList)
