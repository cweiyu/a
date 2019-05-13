
# coding: utf-8

# In[16]:


def reverse(word):
    answer = ''
    for i in word:
            answer = i + answer
    return(answer)
a= reverse("junyiacademy")
print(a)

# In[19]:


def reverse_2(word):
    word = word + " "
    alist = list() 
    answer_2 = ''
    for i in word:
        if i != ' ':
            answer_2 = answer_2 + i
        if i == ' ':
            alist.append(answer_2)
            answer_2 = ''
    for d in alist:
        print(reverse(d))
reverse_2("flipped class room is important")

