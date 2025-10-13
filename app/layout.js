import "./globals.css";

export const metadata = {
  title: "Munchy",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Spicy+Rice&family=Karla&display=swap" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  );
}
