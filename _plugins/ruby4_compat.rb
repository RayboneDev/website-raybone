# Jekyll 3.9 / Liquid 4 still call Ruby's removed taint APIs.
# Keep GitHub Pages' pinned Jekyll usable on Ruby 3.4+ / 4.x.
class Object
  def tainted?
    false
  end unless method_defined?(:tainted?)

  def taint
    self
  end unless method_defined?(:taint)

  def untaint
    self
  end unless method_defined?(:untaint)
end
