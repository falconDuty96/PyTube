# pytube

pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos

## Installation

This guide assumes you already have python and pip installed.

To install pytube, run the following command in your terminal:

```bash
$ pip install pytube
```

## Get the Source Code
pytube is actively developed on GitHub, where the source is available.

You can either clone the public repository:


```bash
$ git clone git://github.com/pytube/pytube.git
```

## Or, download the tarball:
```bash
$ curl -OL https://github.com/pytube/pytube/tarball/master
# optionally, zipball is also available (for Windows users).
```
Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running:

```bash
$ cd pytube
$ python -m pip install .
```


## Usage

```python
from pytube import YouTube
YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams
... .filter(progressive=True, file_extension='mp4')
... .order_by('resolution')
... .desc()
... .first()
... .download()

```
