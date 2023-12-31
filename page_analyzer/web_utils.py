from urllib.parse import urlparse
from validators.url import url as is_correct_url


def get_main_page_url(url: str) -> str:
    """Truncates the URL to the <protocol>://<domain name> structure"""
    parsed_url = urlparse(url)
    return f'{parsed_url.scheme}://{parsed_url.netloc}'


def validate_url(url: str) -> list:
    """Validate url by rules"""
    errors = []

    if not url:
        errors.append('URL обязателен')
    elif len(url) > 255:
        errors.append('URL превышает 255 символов')
    elif not is_correct_url(url):
        errors.append('Некорректный URL')

    return errors
