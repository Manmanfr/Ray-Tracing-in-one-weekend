
import numpy as np
from PIL import Image
import vec3
import color
from ray import ray

def ray_color(r):
    if hit_sphere(vec3.vec3(0, 0, -1), 0.5, r):
        return vec3.vec3(1, 0, 0)

    unit_direction = r._direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * vec3.vec3(1.0, 1.0, 1.0) + t * vec3.vec3(0.5, 0.7, 1.0)

def hit_sphere(center, radius, r):
    oc= center - r._origin
    a= r._direction.length_squared()
    b= -2 * oc.dot(r._direction)
    c= oc.length_squared() - radius * radius
    discriminant= b * b - 4 * a * c
    return discriminant > 0

aspect_ratio = 16.0 / 9.0
image_width = 400

image_height = int(image_width / aspect_ratio)
if image_height <= 1:
    image_height = 1

focal_length = 1.0
viewport_height = 2.0
viewport_width = aspect_ratio * viewport_height
camera_origin = vec3.vec3(0, 0, 0)

viewport_horizontal = vec3.vec3(viewport_width, 0, 0)
viewport_vertical = vec3.vec3(0, -viewport_height, 0)

pixel_delta_x = viewport_horizontal / (image_width)
pixel_delta_y = viewport_vertical / (image_height)

viewport_upper_left = camera_origin - viewport_horizontal / 2 - viewport_vertical / 2 - vec3.vec3(0, 0, focal_length)

pixel00 = viewport_upper_left + pixel_delta_x / 2 + pixel_delta_y / 2

print("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

canvas= np.zeros((image_height, image_width, 3), dtype=np.uint8)

for i in range(image_height):
    print(f"Scanlines remaining: {image_height - i - 1}")
    for j in range(image_width):
        pixel_center = pixel00 + pixel_delta_x * j + pixel_delta_y * i
        r = ray(camera_origin, pixel_center - camera_origin)

        pixel_color = ray_color(r)
        canvas[i, j] = [int(255.999 * pixel_color.x), int(255.999 * pixel_color.y), int(255.999 * pixel_color.z)]
        print(color.write_color(pixel_color))

image= Image.fromarray(canvas)
image.save("output.png")