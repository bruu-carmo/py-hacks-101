# Conversão de RGB para código hexadecimal

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print(rgb_to_hex(255, 0, 128))  # #ff0080

# Outra versão
from webcolors import name_to_hex

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code
    except ValueError:
        return None

colorname = input("Enter color name : ")
result_code = color_name_to_code(colorname)
print(result_code)
