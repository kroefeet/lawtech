from string import Template
top_bottom_text = open('templates/top_bottom.html').read()
template = Template(top_bottom_text)


regenerate = input("Rgenerate site? (yes/no) ")

if regenerate.lower() == 'yes':
	#index page	
	index_page = open('content/index.html').read()
	index_html = template.safe_substitute(
		title="Home",	
		home_class="active",
		content=index_page,
	)	
	open('docs/index.html', 'w+').write(index_html)
	#projects page
	projects_page = open('content/projects.html').read()
	projects_html = template.safe_substitute(
		title="Projects",	
		projects_class="active",
		content=projects_page,
	)	
	open('docs/projects.html', 'w+').write(projects_html)
	#contact page
	contact_page = open('content/contact.html').read()
	contact_html = template.safe_substitute(
		title="Contact me",	
		contact_class="active",
		content=contact_page,
	)	
	open('docs/contact.html', 'w+').write(contact_html)
	
	print("Your site was regenerated. The new pages are in the docs/ folder")
else:
	print("Your site was not regenerated.")	
	



