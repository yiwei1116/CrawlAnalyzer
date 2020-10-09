import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'ptt',
            '-o',
            'gossipe.json'
        ]
    )

except SystemExit:
    pass
