
def create_sxript(d):
    inline = ''
    params = ''
    i = 0
    for k, v in d.items():
        i += 1
        inline += '''"ctx._source[params.field{0}] = params.value{0}",'''. format(i)
        params +='''"field{0}": "{1}","value{0}": {2},'''.format(i,k,v)

    script = '''"inline": {0}"params": {1}'''.format(inline,params)
    return script


def create_id():
    import random
    import string
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random
