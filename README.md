# Get YouTube Thumbnails

This is a web app that gets thumbnail images for YouTube videos. Paste in a YouTube URL and it gives you the thumbnails that are available for that video.

It works with URLs at these YouTube addresses: <code>https://www.youtube.com</code>, <code>https://youtube.com</code>, <code>https://youtu.be</code>, and <code>https://youtube-nocookie.com</code>.

When you submit a YouTube URL, you get back the image, a link to that image, and the original height and width of that image (even if it's scaled down on your screen size).

## Use cases

**Linking to YouTube videos** when you can't or don't want to embed a video

- in emails
- in websites where you don't want any Javascript
- in websites where you want to minimise data transfers

## Installation

- `git clone` this repository
- `pipenv install`
- Add a file called `.env` that looks something like this.

```env
SECRET_KEY="long-string-of-text"
YOUTUBE_API_KEY="your-google-api-key"
CLOUDINARY_CLOUD_NAME="your-cloudinary-cloud-name"
CLOUDINARY_API_KEY="your-cloudinary-api-key"
CLOUDINARY_API_SECRET="your-cloudinary-api-secret"
```

For local development, add a line to the `.env` file saying `FLASK_DEBUG=1`

## Built with

It relies heavily on the YouTube API for getting URLs to thumbnails and on [Cloudinary](https://cloudinary.com) for fetching the images and applying the play logos over the top.

### Python

- Validate YouTube URLs
- Get the correct YouTube video ID for the different types of YouTube URLs
- Build the correct link to the image thumbnails

### Flask

- Templating HTML with Jinja2
- Get URL out of form and send for processing in Python script
- Get results of Python script and put it into HTML

### Javascript

- Fill the input field with the demo link
