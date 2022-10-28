#The author's name is Ellen Kevin
def count_hashtag(string,target):
    total=0
    index=0
    while index<len(string):
        if string[index:index+len(target)]==target:
            total+=1
            index+=len(target)
        else:
            index+=1
    return total



print(count_hashtag('Happy# Birthday# to# you#', '#'))
