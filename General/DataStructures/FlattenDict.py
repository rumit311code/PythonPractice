def flatten_dict(d, parent_key='', sep='_'):
    items = []
    print(f"flatten_dict START: d: {d}, parent_key: {parent_key}, items: {items}")
    for k, v in d.items():
        print(f"==== ====For loop START: k: {k}, v: {v}, items: {items}")
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
        print(f"==== ====For loop END: k: {k}, new_key: {new_key}, v: {v}, items: {items}")
    print(f"flatten_dict END: d: {d}, parent_key: {parent_key}, items: {items}")
    return dict(items)

data1 = {
    "x": {
        "y": {
            "z": 1,
            "w": 2
        },
        "a": 3
    },
    "x1": 13
}
print(flatten_dict(data1))
# {'x_y_z': 1, 'x_y_w': 2, 'x_a': 3, 'x1': 13}
