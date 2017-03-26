def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link<0:
                    url,end_quote=None,0
    else:
         start_quote = page.find('"', start_link)
         end_quote = page.find('"', start_quote + 1)
         url = page[start_quote + 1:end_quote]
    return url, end_quote
url,endpos=get_next_target('mood')   
def get_all_links(page):
    links=[]
    while True:
        url,nextpos=get_next_target(page)
        if url:
            links.append(url)
            page=page[endpos:]
            print link
        else:
          break
    return links
def crawl_web(seed):
    tocrawl=[seed]
    crawled=[]
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled:
            crawled.append(tocrawl)
            crawl.append(get_all_links)
            crawled.append(page)
            return crawled
            