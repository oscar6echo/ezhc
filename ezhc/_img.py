
import requests
import base64

requests.packages.urllib3.disable_warnings()


def is_http_url(img_path):
    img_path = img_path.lower()
    return (img_path.startswith("http://") or
            img_path.startswith("https://"))


def image_base64(imgpath):
    with open(imgpath, 'rb') as obj:
        return base64.b64encode(obj.read()).decode('utf-8')


def image_content(img_path):
    """Get the image content according to its path
    Different case:
      - PNG,JPEG: convert it to base64
      - SVG: open it and read it
      - HTTP URL: get the content via requests.get
    """
    if is_http_url(img_path):
        content = requests.get(img_path, verify=False).content
        if img_path.endswith(".svg"):
            return content
        return base64.b64encode(content).decode('utf-8')
    if img_path.endswith(".svg"):
        return open(img_path).read()
    return image_base64(img_path)


def image_src(img_path):
    content = image_content(img_path)
    if img_path.endswith('.svg'):
        return '{}'.format(content)
    else:
        return 'data:image/png;base64,{}'.format(content)
