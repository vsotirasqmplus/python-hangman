def heading(text, level=1):
    heading_mark = '#'
    level = int(level)
    if level < 1:
        level = 1
    if level > 6:
        level = 6
    return (heading_mark * level) + ' ' + text
