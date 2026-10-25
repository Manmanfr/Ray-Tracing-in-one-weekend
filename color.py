from vec3 import vec3

color = vec3

def write_color(pixel_color):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    return f"{int(255.999 * r)} {int(255.999 * g)} {int(255.999 * b)}"


