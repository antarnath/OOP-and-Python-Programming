import pyjokes

def tell_some_jokes(My_joke):
    print(My_joke)


My_joke = pyjokes.get_joke(language="en",category="neutral")
tell_some_jokes(My_joke)
