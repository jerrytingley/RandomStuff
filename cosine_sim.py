from __future__ import division

def dot(a, b):
    s = 0
    for x, y in zip(a, b): s += x * y
    return s

def norm(a):
    return (dot(a, a))**(1/2)

def sim(a, b):
    return ((dot(a,b))/(norm(a) * norm(b)))

def word_freq(words):
    d = {}
    for word in words: d[word] = d.get(word, 0)+1
    return d

def text_sim(a, b):
    a = a.translate(None, '.,;:1234567890-+\\<>').split()
    b = b.translate(None, ',.;:1234567890-+\\<>').split()
    af, bf = word_freq(a), word_freq(b)
    dv1, dv2 = {}, {}
    all_words = set(a+b)
    for word in all_words:
        if word in af: dv1[word] = af.get(word, 0)
        else: dv1[word] = 0
        if word in bf: dv2[word] = bf.get(word, 0)
        else: dv2[word] = 0
    return sim(dv1.values(), dv2.values())
