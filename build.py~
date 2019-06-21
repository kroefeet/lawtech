def main():
	
	pages = [
		{
			"filename": "content/index.html",
			"output": "docs/index.html",
			"title": "Home",
			"nav_class": "home",
		},
		{
			"filename": "content/projects.html",
			"output": "docs/projects.html",
			"title": "Projects",
			"nav_class": "projects",
		},
		{
			"filename": "content/contact.html",
			"output": "docs/contact.html",
			"title": "Contact me",
			"nav_class": "contact",
		},	
	
	]
	
	
	from string import Template
	top_bottom_text = open('templates/top_bottom.html').read()
	template = Template(top_bottom_text)
	
	
	regenerate = input("Rgenerate site? (yes/no) ")
	
	if regenerate.lower() == 'yes':
		for page in pages:
			new_page = open(page["filename"]).read()	
			page_html = template.safe_substitute(
				title=page["title"],
				content=new_page
				page["nav_class"]+"class"="active"
							
			)	
			open(page["output"], 'w+').write(page_html)
		
		
		print("Your site was regenerated. The new pages are in the docs/ folder")
	else:
		print("Your site was not regenerated.")	
		
if __name__ == "__main__":
	main()


