import requests 
import shutil
import urllib.request

#image_url = "https://images-ssl.gotinder.com/u/5yGjqZHMZZUqtfRUvmg1Vk/6Jt…PHEuicJb0Gb4O21SwCPbGkdpvSj3x4A__&Key-Pair-Id=K368TLDEUPA6OI"
#image_url = "https://images-ssl.gotinder.com/u/qD4NeN3hiXhQs88EYcjKB3/tgjjgZE2giipjnQhSeVWQC.jpg?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS9xRDROZU4zaGlYaFFzODhFWWNqS0IzLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NTAxNDM2MTl9fX1dfQ__&Signature=DH10NXGkNdFEh~kKaQzJMagc2yejOeej0WftZSoxDX8FYvZxeOSWszLFsE-BADZ81FgxKcCTh4v1sJkNJT7s0ogEtgjkzi3JlrKyklV5GkiwooiPQw16LH1N5e5TecJVPyp73w8rZXYSUQCN7uj446THWqcS2RcFv7zd~5r5H5QGHjVZztu60sD0y1GN-efGD76oWO5mA8GVqnfBwZbwFn2dKklXfu6bJ2WndFXx0W6KjiGT5a7kfgEAFDut7DPdiFIz8EGlhEGiV-E6Pp67LGnOE~MK3LiGps8cG5dlFSH11UiE29ZwRreDxsL2DVb7cECq8KRWr98OpcMqjocHuQ__&Key-Pair-Id=K368TLDEUPA6OI"
image_url = "https://images-ssl.gotinder.com/u/PkrrL9J8jaViJuwCHdzcUJ/eiDczhQ2FGyRHecdNrorxF.webp?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS9Qa3JyTDlKOGphVmlKdXdDSGR6Y1VKLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NTAyMTQ5MDZ9fX1dfQ__&Signature=fpKz4dkhwtJY~8o1C4sgJjFtm4jR3BA7kHpsZo2EJzoKTkslzz5KcZ7JNINauYFuFksQGql6Hnb0V6tUF1OnBU7pu3xfAJ~EDpBnD8gAP5CmimaXxw8N1FyrvZuW6dkLjDZ97wYGmceivDlbEPsV0b3inDs7SvXfNyyUAIQ7oL-MH6lIO404tethFCN9H60rA8ZWqVySVQinkBKh7qvRa-0cFEbeaAHXKlBmkH8BK-nxPuWXQEIOYugDs1LwFTyE-jhX4HMxXmucQERhQXBL~zpNj8t53meZDIcFnSrWBIcMqkUdOYG7V13eMGOWeyJ5O~ElOzbvHqRxlj6SpUnSUg__&Key-Pair-Id=K368TLDEUPA6OI"
filename = image_url.split("/")[-1]
r = requests.get(image_url, stream = True)

if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open("imagen3.jpg",'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')