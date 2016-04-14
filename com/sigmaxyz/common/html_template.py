#! /usr/bin/env python

class html_template:
    
    def writeHtml(self, title, body):
        print("Content-type: text/html\n")
        html = "<html><head><title>%s</title></head><body>%s</body></html>"
        print(html % (title,body))
    