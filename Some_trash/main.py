class Zv:

    def __call__(self, some, *args, **kwargs):
        print(f'Давай {some}')


zv1 = Zv()
zv2 = Zv()

zv1("наберешь")
zv2('кушать')
