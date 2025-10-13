// HOMEPAGE

export default function Home() {
  return (
    <main style={styles.container}>
      <h1 style={styles.title}>Munchy</h1>
      <p style={styles.subtitle}>Know what you eat - instantly.</p>
      <a href="/preferences" style={styles.button}>Get Started</a>
    </main>
  )
}

const styles = {
  container: {
    minHeight: '100vh',
    padding: '3rem',
    backgroundColor: '#F7EDD8',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    fontFamily: "'Arial', sans-serif"
  },
  title: {
    color: '#A13721',
    fontFamily: "'Spicy Rice', normal",
    fontSize: 'clamp(2.5rem, 10vw, 6rem)',
    lineHeight: '130px',
    textAlign: 'center',
    textShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)'
  },
  subtitle: {
    color: '#210706',
    fontFamily: "'Karla', bold",
    fontSize: 'clamp(1.2rem, 8vw, 2rem)',
    lineHeight: '24px',
    textAlign: 'center',
  },
  button: {
    color: '#A13721',
    fontFamily: 'Karla',
    fontSize: 'clamp(2rem, 8vw, 2.5rem)',
    lineHeight: '60px',
    textAlign: 'center',
    textDecoration: 'underline'
  }
};