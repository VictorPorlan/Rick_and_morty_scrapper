def localizar_links(html_index):
    start_link= html_index.find('a href=')
    if start_link == -1:
        return None, 0
    start_quote= html_index.find("'", start_link)
    end_quote= html_index.find("'", start_quote + 1)
    url = html_index[start_quote+1 : end_quote]
    return url, end_quote