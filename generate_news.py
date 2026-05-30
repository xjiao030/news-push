import feedparser
import json
import datetime
import os

RSS_FEEDS = {
    "BBC News (全球政治)": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "Reuters (全球)": "https://www.reutersagency.com/feed/",
    "新华社 (中国)": "http://www.xinhuanet.com/english/rss/worldrss.xml",
    "人民网 (国内政治)": "http://www.people.com.cn/rss/politics.xml",
    "环球网 (国内政治)": "https://www.huanqiu.com/rss/world.xml",
    "雅虎财经 (全球财经)": "https://finance.yahoo.com/news/rssindex",
    "CNBC (商业)": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "新浪财经 (中国财经)": "https://finance.sina.com.cn/rss/openeven.xml",
    "华尔街见闻 (商业)": "https://wallstreetcn.com/rss",
    "中国新闻网 (社会)": "http://www.chinanews.com/rss/rss.xml"
}

def fetch_news():
    articles = []
    for source, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                title = entry.get("title", "")
                link = entry.get("link", "")
                published = entry.get("published", datetime.datetime.now().isoformat())
                summary = entry.get("summary", "")
                # 去掉HTML标签
                import re
                summary = re.sub(r'<.*?>', '', summary)[:200]
                articles.append({
                    "source": source,
                    "title": title,
                    "link": link,
                    "time": published,
                    "desc": summary
                })
        except Exception as e:
            print(f"{source} 抓取失败: {e}")
    return articles

if __name__ == "__main__":
    print("抓取新闻中...")
    articles = fetch_news()
    print(f"共获取 {len(articles)} 条新闻")
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print("已生成 news.json")
