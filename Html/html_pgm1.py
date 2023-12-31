from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_startag(self,tag,attrs):
        print("Found tag:",tag)
        print(" Attributes: ",attrs)
    
    def handle_endtag(self, tag):
        print("End tag: ",tag)


data = '<html> <body></body><p class="para text" id ="1"> This is a <b>test</b></p></html>'
parser = Parser()
parser.feed(data)

