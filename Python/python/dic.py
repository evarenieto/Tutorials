def packer(**kwars): #the double ** makes a dict from the arguments
    print(kwars)

packer(name='eva', age='28',she_s_from='spain')



def packer(name=None,**kwars):
    print(kwars)

packer(name='eva', age='28',she_s_from='spain')


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")
unpacker(**{'last_name':'love', 'first_name':'kekneth'})
