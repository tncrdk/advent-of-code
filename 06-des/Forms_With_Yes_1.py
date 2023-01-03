def Formatting(link):
    with open(link) as f:
        txt = f.read().split("\n\n")
    txt = [i.split("\n") for i in txt]
    return txt


def FindDistinctAnswers(Answers: list):
    UniqueAnswers = set(())
    for i in Answers:
        UniqueAnswers = UniqueAnswers | set(i)

    return UniqueAnswers


def FindCount(AnswersList):
    count = 0
    for i in AnswersList:
        count += len(FindDistinctAnswers(i))

    print(count)


link = (
    "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\06-des\\Form_Answers.txt"
)

AnswersList = Formatting(link)

FindCount(AnswersList)
