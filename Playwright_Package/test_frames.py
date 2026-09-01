from playwright.sync_api import Page
import time
class TestFrameMethods:
    def test_frame(self,page:Page):
        page.goto("http://demoqa.com/frames")
        time.sleep(2)
        iframe_1= page.frame_locator("#frame1")
        print(iframe_1.locator("#SampleHeading").text_content())
        print("sucessfully switched into frame 1")
