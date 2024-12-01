/** @type {import('tailwindcss').Config} */
import defaultTheme from 'tailwindcss/defaultTheme';

module.exports = {
  darkMode: "class",
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    './node_modules/@chakra-ui/react/**/*.{js,jsx,ts,tsx}'
  ],
  theme: {
    extend: {
      screens: {
        'sm': '480px',
        'md': '768px',
        'lg': '976px',
        'xl': '1440px'
      },
      colors: {
        'primary': {
          DEFAULT: '#EF5528',
          100: '#fac7b8',
          200: '#f6a188',
          300: '#f37c59',
          400: '#ef5629',
          500: '#d63d10',
          600: '#a62f0c',
          700: '#772209',
          800: '#471405',
          900: '#180702'
        },
        'secondary': {
          DEFAULT: '#0094DA',
          100: '#b3e6ff',
          200: '#b3e5ff',
          300: '#80d6ff',
          400: '#4dc6ff',
          500: '#1ab5ff',
          600: '#009ce6',
          700: '#0079b3',
          800: '#005780',
          900: '#00344d',
        },
        'gray': {
          DEFAULT: '#d2d6dc',
          100: '#f4f5f7',
          200: '#e4e7eb',
          300: '#d2d6dc',
          400: '#9fa6b2',
          500: '#6c798f',
          600: '#4b5563',
          700: '#374151',
          800: '#252f3f',
          900: '#161c2d'
        },
        'gray-light': '#d3dce6'
      },
      fontFamily: {
        'ubutntu': ['Ubuntu', ...defaultTheme.fontFamily.sans],
      },
      extend: {
        'spacing': {
          '128': '32rem',
          '144': '36rem'
        },
        'borderRadius': {
          '4xl': '2rem'
        }
      }
    }
  },
  plugins: [],
  'include': ['src/**/*', 'src/custom.d.ts']
};
