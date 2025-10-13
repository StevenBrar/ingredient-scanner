

export default function Header() {
    return (
        <header style={styles.header}>
        <img src="/logo.svg" alt="Munchy Logo" style={styles.logo}/>
        <a href="/about" style={styles.aboutLink}>About</a>
        </header>
    );
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
}