# Raybone Company Website

This website is hosted on GitHub Pages, using the Jekyll static site builder. The site's main language is Farsi, with a synchronized English version of every page under the `/en/` prefix.

The Raybone blog is created using posts in `_posts` directory. There is also a knowledge base that has a blog-like structure (but without date) and is created with the content of `_knowledge`.

## Development

Install Ruby development tools:
```sh
apt install ruby ruby-dev ruby-bundler build-essential zlib1g-dev
```

Then run provided just commands for running the project:

```sh
just install  # Install project dependencies
just serve    # Start the development server
```

The local compatibility plugins (in `_plugins/`) support the GitHub Pages dependencies on newer Ruby versions.

The `just` commands keep Bundler's project configuration in `.bundle/` and user files in `.bundle/user/`, so they do not require a writable home directory.
