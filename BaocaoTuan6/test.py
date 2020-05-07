from bs4 import BeautifulSoup

html = '''<div data-testid="post_message" class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}" id="js_8e"><p>In acute cases corona virus can kill within seven days after occurrence of symptoms</p></div>'''

soup = BeautifulSoup(html, "html.parser")
content_post = soup.find(
    "div", {"class": "_5pbx userContent _3576"})
print(type(content_post.get_text()))
