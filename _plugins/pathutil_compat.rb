# GitHub Pages pins Pathutil 0.16.2, whose read method forwards keyword
# options as a positional Hash. Ruby 3 rejects that when the watcher reads
# /proc/version to detect the platform. Keep its encoding and newline behavior.
require "pathutil"

if RUBY_VERSION >= "3.0" && Gem.loaded_specs["pathutil"].version == Gem::Version.new("0.16.2")
  module RaybonePathutilReadCompatibility
    def read(*args, **options)
      options[:encoding] ||= encoding
      content = File.read(self, *args, **options)
      normalize[:read] ? content.encode(universal_newline: true) : content
    end
  end

  Pathutil.prepend(RaybonePathutilReadCompatibility)
end
