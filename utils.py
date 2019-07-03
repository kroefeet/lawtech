import glob
import os
from jinja2 import Template

#get current year for footer copyright
import datetime
d = datetime.datetime.today()
year = (d.year)


#populate pages dictionary for templating
def get_page_list():
	pages = []
	all_files = glob.glob("content/*.html")
	all_blog_posts = glob.glob("blog/*.html")
	
	#populate pages dictionary with all main pages
	for file in all_files:
		filename = os.path.basename(file)
		title, extension = os.path.splitext(filename)
		pages.append(
			{
			"content" : file,	
			"output" : "docs/" + filename,
			"title" : title,	
			"blog_title" : ''		
			}	
		)
	
	#populate pages dictionary with all blog post content	
	for blog_post in all_blog_posts:
			blog_file = os.path.basename(blog_post)
			blog_title, extension = os.path.splitext(blog_file)	
			pages.append(
				{
				"content" : blog_post,
				"output" : "docs/blog_" + blog_file,
				"title" : "blog",
				"blog_title" : blog_title,				
				}			
			)

	return pages
	



# apply templating and make the page
def make_page(pages):
	base = open('templates/base.html').read()
	main_template = Template(base)

	for page in pages:
			new_page = open(page["content"]).read()
		
			
		#This part updates the navbar link highlighting
			if page['title'] == "index":	
					extra_kws = {"home_class":"active"}				
			elif page['title'] == "contact":
					extra_kws = {"contact_class":"active"}	
			elif page['title'] == "projects":
					extra_kws = {"projects_class":"active"}		
			else:	
					extra_kws = {"blog_class":"active"}	
		
			
			page_html = main_template.render(
					title=page['title'],
					content=new_page,
					copy_year = year,
					blog_title=page['blog_title'],
					**extra_kws,
					)
						
			open(page["output"], 'w+').write(page_html)
			
#	This will create a new placeholder page in the content directory
def create_placeholder(string):
	placeholder_content= """
			<h1>New Content!</h1>
			<p>New content...</p>	
		"""	
	
	if string.lower() == 'new':	
		open("content/new_content_page.html", 'w+').write(placeholder_content)
		print("Your placeholder page is in the content/ folder.")
	elif string.lower() == 'blog':
		open("blog/new_content_page.html", 'w+').write(placeholder_content)
		print("Your placeholder blog post is in the blog/ folder.")
	else:
		print("The program didn't get that. Try again. ")

			
#This will run if a user wants to generate or regenerate the website using templates		
def re_generate():			
	pages = get_page_list()

	regenerate = input("Regenerate site? (yes/no) ")
	
	if regenerate.lower() == 'yes':
		make_page(pages)
		print("Your site was regenerated. The new pages are in the docs/ folder")
	else:
		print("Your site was not regenerated.")	
		
		
		