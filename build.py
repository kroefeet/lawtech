top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

page_name = input("What is the name of your content file? ")

page = open('content/'+page_name).read()
#print(page)
# print(top)
new_page = (top + page + bottom)

open('docs/'+page_name, 'w+').write(new_page)
print("Your page should now be available here: docs/{}".format(page_name))
