f= open("english_ann.txt","r+", encoding="utf-8")
text = f.read()
c= ""
for i in range(1, len(text)):
    if text[i-1]=="\n":
        c+=text[i].lower()
    else:
        c+=text[i]
f.seek(0)
f.write(c)
f.close()