class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        import re
        links = re.findall(r'href\s*=\s*("|\')+([^"\'>\s]*)', content, re.I)
        return [link[1] for link in links if len(link[1]) and not link[1].startswith('#')]