import cv2
import time
from blue_sbc.screen.classes import Screen
from blue_sbc.algo.golpy import GoLpy

golpy = GoLpy(7, 17)


class Scroll_Phat_HD(Screen):
    def show(
        self,
        image,
        session,
        header=[],
        sidebar=[],
    ):
        super(Scroll_Phat_HD, self).show(
            image,
            session,
            header,
            sidebar,
        )

        if session.add_timer("scroll_phat_hd", 1.0 / 3):
            golpy.re_init()

        if session.new_frame:
            golpy.init(session.frame_image)

        if session.timer["scroll_phat_hd"].tick():
            import scrollphathd

            for x in range(0, 17):
                for y in range(0, 7):
                    scrollphathd.set_pixel(x, y, golpy.grid(x, y))

            time.sleep(0.01)
            scrollphathd.show()

            if golpy.blank():
                golpy.re_init()
            else:
                golpy.progress()

        return self
