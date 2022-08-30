
def encode_to_base_62(num: int, alphabet):
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append
    _divmod = divmod
    base = len(alphabet)
    while num: 
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return "".join(arr)