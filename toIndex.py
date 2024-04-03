import markdown


file_path = "第六周401-407.md"
html_path = "output.html"

with open(file_path, 'r', encoding="utf-8") as file:
    md_text = file.read()


html = markdown.markdown(md_text)

print(html)

with open(html_path, 'w', encoding='utf-8') as file:
    file.write(html)

