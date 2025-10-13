import "./globals.css";
import Header from './components/Header.js';

export const metadata = {
  title: "Munchy",
  description: 'Know what you eat - instantly.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Spicy+Rice&family=Karla&display=swap" rel="stylesheet" />
      </head>
      <body>
        <Header />
        {children}
      </body>
    </html>
  );
}
