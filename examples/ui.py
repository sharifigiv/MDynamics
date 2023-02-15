from pyray import Color, Vector2, Rectangle, draw_rectangle_lines_ex, draw_text, measure_text, draw_rectangle, check_collision_point_rec

class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.text = text

        self.border_width = 5
        self.border_color = Color(0, 0, 0, 255)

        self.bg_color = Color(255, 255, 255, 255)
        self.bg_hover_color = Color(237, 237, 237, 255)
        self.bg_click_color = Color(214, 214, 214, 255)

        self.text_color = Color(0, 0, 0, 255)
        self.text_size = 18
        self.text_size_px = measure_text(self.text, self.text_size)

        self.rec = Rectangle(self.x, self.y, self.width, self.height)

        self.hovering = False
        self.clicked = False

        self.last_mouse = [0, 0]

    def show(self):
        if self.clicked:
            draw_rectangle(self.x, self.y, self.width, self.height, self.bg_click_color)
        else:
            if not self.hovering:
                draw_rectangle(self.x, self.y, self.width, self.height, self.bg_color)

            else:
                draw_rectangle(self.x, self.y, self.width, self.height, self.bg_hover_color)
                
        draw_rectangle_lines_ex(self.rec, self.border_width, self.border_color)
        draw_text(self.text, self.x + self.width//2 - self.text_size_px // 2, self.y + self.height//2 - 10, self.text_size, self.text_color)

    def update(self, mouse_pos, mouse_down):
        if check_collision_point_rec(Vector2(mouse_pos[0], mouse_pos[1]), self.rec):
            if mouse_down:
                if mouse_pos != self.last_mouse:
                    if self.clicked:
                        self.clicked = False

                    else:
                        self.clicked = True

            self.hovering = True

        else:
            self.hovering = False
