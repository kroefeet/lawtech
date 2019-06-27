# import pages dictionary
from pages import pages
from pages import blog_posts

#get current year for footer copyright
import datetime
d = datetime.datetime.today()
year = (d.year)

# apply templating to blog posts and make blog post page
def add_new_blog_posts(dict):
	from string import Template
	blog = open('templates/blog.html').read()
	blog_template = Template(blog)	
	
	for blog_post in blog_posts:
			#create individual blog post pages
			new_blog_post = open(blog_post["filename"]).read()
			
			blog_html = blog_template.safe_substitute(
					title=blog_post["title"],
					content=new_blog_post,
					date=blog_post["date"],
					copy_year = year,
				)
			
			filename = blog_post["filename"].replace("blog/", "")
			output = "docs/blog_"+filename
	
			open(output, 'w+').write(blog_html)
			



# apply templating and make the page
def make_page(dict):
	from string import Template
	top_bottom_text = open('templates/top_bottom.html').read()
	main_template = Template(top_bottom_text)
			
	
	for page in pages:
			#print(page)
			new_page = open(page["filename"]).read()
			nav_update = page["navclass"]
			#This part updates the navbar link highlighting
			if nav_update == "home_class":	
					extra_kws = {"home_class":"active"}				
			elif nav_update == "contact_class":
					extra_kws = {"contact_class":"active"}	
			elif nav_update == "projects_class":
					extra_kws = {"projects_class":"active"}		
			else:	
					extra_kws = {"blog_class":"active"}	
		
			
			page_html = main_template.safe_substitute(
					title=page["title"],
					content=new_page,
					copy_year = year,
					**extra_kws,
					)
			
						
			open(page["output"], 'w+').write(page_html)

# run functions and create site
def main():
	
	regenerate = input("Regenerate site? (yes/no) ")
	
	if regenerate.lower() == 'yes':
		make_page(pages)
		add_new_blog_posts(blog_posts)
		print("Your site was regenerated. The new pages are in the docs/ folder")
	else:
		print("Your site was not regenerated.")		
	


		
if __name__ == "__main__":
	main()


