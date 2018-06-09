
from gmail import GMail
from gmail import Message
from random import choice
import time

html_content = """
                <p><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Cộng h&ograve;a X&atilde; hội Chủ nghĩa Việt Nam</strong></p>
<p><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<p><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ĐƠN XIN NGHỈ HỌC</strong></p>
<p><strong><br /></strong>Hi Tuấn Anh,</p>
<p>H&ocirc;m nay anh bị {{sickness}} n&ecirc;n xin ph&eacute;p nghỉ học buổi h&ocirc;m nay nh&eacute;.</p>
<p>Thanks.</p>
<p>&nbsp;</p>
"""

sickness_list = ["Cam cum", "dau dau", "dau bung", "nhot trong nha"]
sickness_chosen = choice(sickness_list)
new_html_conent = html_content.replace("{{sickness}}",sickness_chosen)

loop = True

while loop:
    hour = time.strftime("%H")
     if hour == 7:
        gmail = GMail("dummyemail5200","notrealemail")
        msg = Message("Test message 1", to = "allmaterials513@gmail.com", html = new_html_conent)
        gmail.send(msg)
    else:
        break