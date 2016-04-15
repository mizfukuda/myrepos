#! /usr/bin/env python
# coding: utf-8

class html_template:
    
    def writeHtml(self, title, body):
        html = """
            <html>
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
                    <title>%s</title>
                </head>
                <body>%s</body>
            </html>"""
        print(html % (title, body))
    