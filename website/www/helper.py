import markdown2
import os.path

def markdownify(file):
    f = open(os.path.dirname(os.path.abspath(__file__))+'/templates/www/{}.md'.format(file), 'r')
    myfile = f.read()
    f.close()
    return markdown2.markdown(myfile)
