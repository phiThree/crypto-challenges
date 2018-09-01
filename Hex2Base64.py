# converts a hex string into base64

import base64

hex = input('enter:')


def main(hex):
    encoded = base64.b64encode(bytes(hex, "utf-8"))
    assert isinstance(encoded, object), "Input isn't valid"
    print(encoded)


if __name__ == '__main__':
    main(hex)

    
# bug to fix: it works, it just puts out the wrong answer? look into
