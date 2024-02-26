def extract_text(element):
    text = ''
    if element.text:
        text += element.text.strip() + ' '
    for child in element:
        text += extract_text(child)
        if child.tail:
            text += child.tail.strip() + ' '
    return text


def look_for_links(element):
    list = []
    if element.tag.endswith('ptr'):
    #    print(element.tag)
        if element.attrib.get('target','default')[0:4] == 'http':
            list.append(element.attrib['target'])
    for child in element:

        link = look_for_links(child)
        for l in link:
            list.append(l)
    return list