# Keep Bundler configuration and user files inside this project.
export BUNDLE_APP_CONFIG := justfile_directory() / ".bundle"
export BUNDLE_USER_HOME := justfile_directory() / ".bundle/user"

# List available commands.
default:
    @just --list

# Install project dependencies.
install:
    bundle install

# Serve the site locally and rebuild on changes.
serve:
    bundle exec jekyll serve

# Build the static site in _site/.
build:
    bundle exec jekyll build

# Remove generated output and caches.
clean:
    bundle exec jekyll clean
