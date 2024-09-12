FROM ruby:latest
RUN gem install jekyll bundler
WORKDIR /src
ENTRYPOINT bundle update && bundle exec jekyll serve \
  --host 0.0.0.0 --config _config.yml