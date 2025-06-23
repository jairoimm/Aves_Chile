def crear_archivo(template):
    with open('index.html', 'w',  encoding='utf-8') as f:
        return f.write(template)