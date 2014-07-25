Title: Why Use a Static Site Generator Instead of a Blogging Platform
Date: 2014-07-25 15:42
Tags: blogging, static, generator, staticgenerator, development
Slug: why-use-a-static-site-generator
Author: Jorge Escobar
Status: published

<img src="/images/posts/2014/07/static-screen.jpeg" width="450" height="300" class="img-thumbnail" alt="Static Screen" />

When I started using Wordpress, I thought it was an awesome solution for blogging. It was easy to install and seemed like by just using plugins, you could augment your blog with a lot of features easily.

That was until I got hacked not only once, but twice. Wordpress and any other database-backed Content Management System suffers from the same security vulnerability: you store the content behind an authorization scheme. There are ways to prevent this (and I even wrote a [blog post](https://web.archive.org/web/20100213110721/http://jungleg.com/2009/09/21/feeling-secure-with-the-latest-wordpress-version-think-again-and-7-tips-to-secure-it) about it in the previous incarnation of my blog), but the complexity of keeping up to date with all the patches, monitoring bad plugins and other security considerations quickly become pretty overwhelming. The feeling of seeing Viagra ads all over your site is something you don't easily shake.

There's also the scalability factor: if your site has a mention on Mashable or Hacker News, you can pretty much kiss your website goodbye, as your infrastructure is not designed to withstand hundreds of visits per second, and unless you have some sort of caching layer enabled (which most small blogs don't), every page needs to request its content from the database -- and that becomes a bottleneck for the serving of your content.

When I decided to launch my blog again, I knew I wanted to do it using the new wave of content serving systems: static site generators.

#### What is a static site generator?

The idea seems a little bit stange at first. What if instead of generating each post every time the user requests it, we pre-generate *all* the posts, write them on the filesystem as static HTML/CSS/JavaScript files and folders and then transmit that content to the remote server?

But wait, you must be saying, doesn't that take a long time? The truth is for most blogs it doesn't, and unless you have thousands of posts, regenerating a blog with 1,000 posts takes a few seconds for most generators. But the beautiful thing is that once that content is generated, there are no databases to access, your whole site is just a bunch of files and folders.

There are many static site generators, but the most important thing to consider in my opinion is how comfortable you are with the technology that powers it. For example, the most popular Ruby static site generator is [Jekyll](http://jekyllrb.com/), for Go it's [Hugo](http://hugo.spf13.com/), but for me, being a Python fanatic, there was not a whole of good choices until [Pelican](http://blog.getpelican.com/) came along. For a comprehensive list of static site generators check out [this site](http://staticsitegenerators.net/).

Now of course there are some drawbacks for using a static site generator. For one, there's no pretty admin like Wordpress where you have a WYSIWYG editor -- you need to be comfortable editing plain text files on the system. The content file type varies across generators, but most support Markdown, which is a wiki-like spec to style text. Here's a handy [Markup cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Then there's all the setup of the system itself and how you transmit content back to your public server. I will go into some of those details in this post, but specifically centered on the Pelican static site generator.

### Setting up Pelican

There's a great [screencast](http://hackercodex.com/guide/pelican-static-site-generator-install/) that goes into the details of how to install Pelican in your system. Go check it out and then come back for some of the things I found useful.

The Pelican [documentation](http://docs.getpelican.com/en/3.4.0/) is pretty good, so if you get stuck you can refer to it. The most important thing (as in every other Python project) is to setup a virtual environment for you blog, `pip install` the Pelican package and using the handy `pelican-quickstart`, which, through a series of questions, helps you to setup your initial blog shell.

The initial look and feel is not great (I really liked [Octopress'](http://octopress.org/), but hey, I'm not a Ruby guy), but Pelican allows you to install themes, using the command line tool `pelican-themes`. I settled on the awesome [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) since I am knowledgeable with the [Bootstrap framework](http://getbootstrap.com/).

You will need to edit your `pelicanconf.py` to your custom needs. Themes also allow you to put custom tags in there. One of the important decisions will be the URL structure, which I go into in the next section.

Once you have your initial structure, you should initialize a git repository for the folder, as this allows you to have version control of the whole blog and potentially share it with the world.

### Folder structure

You will notice is that you have two main folders in your blog: `content` which holds the files that you will be editing and `output` which is the files that Pelican automatically generates using the files on `content`.

Inside the `content` folder, you'll see a bunch of folders. There's a `posts` folder, which stores the blog archive, the `pages` folder that will house your more static pages, for example your "About" page, `images` which will hold all the images and `extra` where you can put custom files, like a specific css or js files you want to use.

I split the `posts` and `images` folder to follow the archive structure that I put into my `pelicanconf.py` configuration. This is what my URL format looks like:

```python
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
```

So my `posts` folder has `2014` in it, and inside I have `06` and `07` folders (for the June and July posts), and inside those I have the actual Markdown file (for example this post is called `Why Use a Static Site Generator.md`).

###