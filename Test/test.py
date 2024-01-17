from bs4 import BeautifulSoup, SoupStrainer

html_content = """
<html>
    <head> ... </head>
    <body>
        <div class="c0">
            <div class="c1"> .... </div>
            <div class="c2"> .... </div>
            <div class="c3"> .... </div>
        </div>
    </body>
</html>
"""


div_c2_strainer = SoupStrainer("div", class_="c2")
soup = BeautifulSoup(html_content, "html.parser", parse_only=div_c2_strainer)
print(soup.prettify())

