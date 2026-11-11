/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './_includes/**/*.html',
    './_layouts/**/*.html',
    './*.html',
    './about/**/*.html',
    './branding/**/*.html',
    './knowledge/**/*.html',
    './**/*.md'
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Vazirmatn', 'sans-serif'],
      },
      // ... keep your existing animations and keyframes here ...
    }
  },
  plugins: [],
}