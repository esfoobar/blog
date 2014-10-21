Title: Running Flask in Cloud9 with Virtualenv
Date: 2014-10-21 18:00
Tags: development, python, cloud9, flask, virtualenv
Slug: running-flask-in-cloud9-with-virtualenv
Author: Jorge Escobar
Status: published

I've been playing with [Cloud9](https://c9.io) lately and wanted to get a Flask application up and running. In case you don't know about it, Cloud9 offers virtualized Ubuntu instances where you can develop applications and install libraries without paying anything.

Even though Cloud9 offers a ready to go Django environment, I wanted to see how I could get a Flask application up and running. I ran into some issues, specifically with the Python "runner". Runners are basically servers that allow you to see your application in a browser.

Here's what I did step by step.

First create a new hosted workspace with a custom type selected:

<img src="http://jungleg.com/images/posts/2014/10/workspace-select.png" width="450" height="365" class="img-thumbnail" alt="Cloud9 Workspace Select" />

Open a terminal window and in your workspace directory, create the virtualenv and activate it:
```python
virtualenv venv
source venv/bin/activate
```

Install flask:
```python
pip install flask
```

Now create a folder for your project (I'll make it "project") and inside create an index.py:
```python
import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello c9 World!"


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
```

Then right click it and run it, it will throw an error:
```python
Your code is running at https://demo-2-c9-jungleg.c9.io.
Important: use os.getenv(PORT, 8080) as the port and os.getenv(IP, 0.0.0.0) as the host in your scripts!

Traceback (most recent call last):
  File "/home/ubuntu/workspace/project/index.py", line 2, in <module>
    from flask import Flask
ImportError: No module named flask
```

What's happening here is that Cloud9 is running the file with the standard Python binary which is not the same one on our virtualenv. We need to explicitly pass the python in our virtualenv so that it runs correctly.

So, click on the runner and select edit:

<img src="http://jungleg.com/images/posts/2014/10/runner-editor.png"  width="320" height="552" class="img-thumbnail" alt="Cloud9 Runner Editor" />

And edit the file so that it references the right python:
```python
// This file overrides the built-in Python 2.7 runner
// For more information see http://docs.c9.io:8080/#!/api/run-method-run
{
  "cmd": [
    "/home/ubuntu/workspace/venv/bin/python",
    "$file",
    "$args"
  ],
  "selector": "^.*\\.(python|py)$",
  "info": "Your code is running at \\033[01;34m$url\\033[00m.\n\\033[01;31mImportant:\\033[00m use \\033[01;32mos.getenv('PORT', 8080)\\033[00m as the port and \\033[01;32mos.getenv('IP', '0.0.0.0')\\033[00m as the host in your scripts!\n"
}
```
Save it and now run the file again. You should see your Flask app up and running.
