from random import choice as rand

def generate_random_url():
    url = 'http://imgur.com/'
    for i in range(5): url += rand('abcdefghijklmnopkrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return url

def generate_html(num, file_out):
    with open(file_out, 'w') as f:
        for i in range(num):
            url = generate_random_url()
            f.write('<a href="'+url+'">'+url+'</a><br/>\n')
