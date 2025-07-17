from modules.crawler.utils import parserTargetURL
from modules.crawler.utils import run
from posts.models import Post

data = run(board='Baseball', pageNum='19621')

for article in data:
    article_model = Post(
        title=article.title,
        slug=article.url,
        content=article.content
    )
    article.save()

print(data)