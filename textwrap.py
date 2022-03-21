import textwrap

def wrap(string, max_width):
    text = textwrap.wrap(string, max_width)
    return "\n".join(text)

if __name__ == '__main__':
