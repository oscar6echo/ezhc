
import requests
import base64

from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()


def all_images(html):
    soup = BeautifulSoup(html)
    imgs = soup.find_all('img')
    return list({t.attrs['src'] for t in imgs})


def is_http_url(img_path):
    img_path = img_path.lower()
    return (img_path.startswith("http://") or
            img_path.startswith("https://"))

def image_base64(imgpath):
    with open(imgpath, 'rb') as obj:
        return base64.b64encode(obj.read())


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
        return base64.b64encode(content)
    if img_path.endswith(".svg"):
        return open(img_path).read()
    return image_base64(img_path)


def replace_imgpath_by_content(html, image_path):
    for path in image_path:
        content = image_content(path)
        if path.endswith(".svg"):
            html = html.replace('<img alt="alt text" src="{}" />'.format(path),
                                '{}'.format(content))
        else:
            html = html.replace('src="{}"'.format(path),
                                'src="data:image/png;base64,{}"'.format(content))
    return html


def embed_img(html):
    image_paths = all_images(html)
    output = replace_imgpath_by_content(html, image_paths)
    return output

    