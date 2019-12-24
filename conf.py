# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "sourbell/project@gh-pages"
}

# 站点设置
site_name = "豪猪尾巴"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-24T23:19+08:00"
author = "Bristletail"
email = "i@sourbell.im"
author_homepage = "https://sourbell.im"
description = "Alive"
key_words = ['Maverick', 'sourbell', 'Bristletail', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/sourbell",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/sourbell",
        "icon": "gi gi-github"
    },
    {
        "name": "Steam",
        "url": "https://steamcommunity.com/id/sourbell/",
        "icon": "gi gi-steam"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
