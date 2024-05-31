from pygame import Surface, image, transform
from util import DisplayMode, Vec, Angle


class Image:
    """ Pygame Image """
    position: Vec
    """ Position of the image """
    dimension: Vec
    """ Dimensions of the image """
    image: str
    """ Image file location """
    rotation: Angle
    """ Rotation of image """
    data: Surface

    def __init__(self, position: Vec, dimension: Vec, img: str, rotation: Angle = None):
        if rotation is None:
            rotation = Angle(degree=0)
        self.position = position
        self.dimension = dimension
        self.image = img
        self.rotation = rotation
        image_data = image.load(self.image).convert()
        image_data.set_colorkey((0, 0, 0))
        self.img = transform.scale(image_data, (self.dimension.w, self.dimension.h))

    def display(
            self,
            screen: Surface,
            display_mode: DisplayMode,
            camera_offset: Vec
        ):
        image = transform.rotate(self.img, -self.rotation.degree)
        screen.blit(
            image,
            self.position.offset_new(*camera_offset.sep()).offset(
                -self.dimension.w/2
                    if display_mode == DisplayMode.CENTER else 0,
                -self.dimension.h/2
                    if display_mode == DisplayMode.CENTER else 0
            ).sep()
        )
