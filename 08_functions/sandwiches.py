def f_ingredients(*args):
    print(args)

def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

def make_car(brand, model, **params):
    params['']

f_ingredients('salami', 'cheese')
info = build_profile('Daniel', 'Jarosz', occupation='debil')
print(info)