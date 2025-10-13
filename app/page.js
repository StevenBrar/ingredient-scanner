// HOMEPAGE

export default function Home() {
  return (
    <>
    <header style={styles.header}>
      <img src="/logo.svg" alt="Munchy Logo" style={styles.logo}/>
      <a href="/about" style={styles.aboutLink}>About</a>
    </header>

    <main style={styles.container}>
      <h1 style={styles.title}>Munchy</h1>
      <p style={styles.subtitle}>Know what you eat - instantly.</p>
      <a href="/preferences" style={styles.button}>Get Started</a>
    </main>

    </>
  )
}

const styles = {
  header: {
    width: '100%',
    padding: '1rem 2rem',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#F7EDD8',
    position: 'absolute',
    top: 0,
    left: 0,
  },
  logo: {
    height: '90px'
  },
  aboutLink: {
    fontFamily: "'Spicy Rice', normal",
    fontSize: '2.5rem',
    color: '#A13721',
    textDecoration: 'none',
    lineHeight: '44px',
    padding: '1rem 2rem',
  },
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