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

def hash_spam():
    if count_hashtag()>4:
        print("This tweet willbe considered as a spam!")
    else:
        print(count_hashtag())

count_hashtag()=5
hash_spam
