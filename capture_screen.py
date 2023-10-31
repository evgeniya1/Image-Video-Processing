from mss import mss, tools
import time
from datetime import datetime

#schedule screenshots
# with mss() as screen:
#     for i in range(3):
#         date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         screen.shot(output=f'screenshot_{date}.png')
#         time.sleep(1)

#part of the screen
with mss() as screen:
    part = {'top':257, 'left':900, 'width':500, 'height':400}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output='screenshot_partial.png')