# Proxy Scrapper

## Example

```text
$ python3 proxy_scrapper.py
```

The script silently fetches the proxy table from free-proxy-list.net and appends
each discovered proxy to `proxies.txt`:

```text
185.199.228.220:7300
103.149.162.195:80
47.74.152.29:8888
...
```

No interactive prompts are shown; all output goes directly into the file.

Install BeautifulSoup
```sh
pip3 install beautifulsoup4
```

Run script
```sh
python3 proxy_scrapper.py
```

## Dependencies

- requests
- beautifulsoup4
