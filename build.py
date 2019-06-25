# import pages dictionary
from pages import pages
from pages import blog_posts

#get current year for footer copyright
import datetime
d = datetime.datetime.today()
year = (d.year)

# add new item to pages dict to be included in site generation
#def add_new_blog_post(dict):
#	from string import Template
#	blog_base_text = open('blog_base.html').read()
#	template = Template(blog_base_text)	
#	
#	for blog_post in blog_posts:
#			#create individual blog post pages
#			new_blog_post = open(blog_post["filename"]).read()
#			
#	filename = input("What is the filename as found in the blog folder? ")
#	output = "docs/blog_"+filename
#	title = input("What would you like the title to be? (limit to 2 words) ")
#	navclass = "blog_class"
#	blog_post = {
#						"filename": "blog/"+filename,
#						"output": output,
#						"navclass": "blog_class"
#						"title" : 
#					} 
#	pages.append(dict(blog_post))
#	#print(blog_post)	
#	#open("pages.py", 'w+').append(blog_post)
#	# TODO: How to write this dictionary to the external pages list in pages.py
#	return
	


	
# apply templating and make the page
def make_page(dict):
	from string import Template
	top_bottom_text = open('templates/top_bottom.html').read()
	template = Template(top_bottom_text)	
	
	for page in pages:
			#print(page)
			new_page = open(page["filename"]).read()
			nav_update = page["navclass"]
			if nav_update == "home_class":	
				page_html = template.safe_substitute(
					title=page["title"],
					content=new_page,				
					home_class="active",
					copy_year = year,
				)
			elif nav_update == "contact_class":
				page_html = template.safe_substitute(
					title=page["title"],
					content=new_page,
					contact_class = "active",
					copy_year = year,
				)
			elif nav_update == "projects_class":
				page_html = template.safe_substitute(
					title=page["title"],
					content=new_page,
					projects_class = "active",
					copy_year = year,
				)
			else:
				page_html = template.safe_substitute(
					title=page["title"],
					content=new_page,
					blog_class = "active",
					copy_year = year,
				)
			
			open(page["output"], 'w+').write(page_html)

# run functions and create site
def main():
#	add_new = input("Would you like to add a new blog post to the list? (yes/no) ")
#	if add_new.lower() == "yes":
#		add_new_blog_post()
#		print("New page added for site regeneration. ")
#		#print(pages)
#		
#	else:
#		print("No new pages added for site regeneration. ")	
	
	regenerate = input("Regenerate site? (yes/no) ")
	
	if regenerate.lower() == 'yes':
		make_page(pages)
		print("Your site was regenerated. The new pages are in the docs/ folder")
	else:
		print("Your site was not regenerated.")		
	


		
if __name__ == "__main__":
	main()


