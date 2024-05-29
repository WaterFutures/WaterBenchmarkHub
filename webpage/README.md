# Webpage of the WaterBenchmarkHub

This folder contains the webpage (i.e. UI) of the WaterBenchmarkHub.

The webpage is realized using the *Vue.js* and *bootstrap* frameworks, and is deployed using GitHub pages -- available at [https://waterfutures.github.io/WaterBenchmarkHub](https://waterfutures.github.io/WaterBenchmarkHub).

## Publish webpage on GitHub pages

In order to publish the webpage, this fodler (i.e. `webpage/`) must be pushed to the `gh-pages` branch.

## Build and run webpage locally

The following steps describe how to build and test the webpage locally:

1. Make sure you have ruby-dev, bundler, and nodejs installed -- i.e. on Ubuntu you run:
```
sudo apt install ruby-dev ruby-bundler nodejs
```
2. Install ruby dependencies:
```
bundle install --path .vendor/bundle
```

3. Build the website -- this creates a folder `_site` contanining everything:
```
bundle exec jekyll build
```

4. Build & Run website:
```
bundle exec jekyll serve
```
