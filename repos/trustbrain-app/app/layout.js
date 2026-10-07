import './globals.css'

export const metadata = {
  title: 'TrustBrain™ — Autonomous Security Reasoning Copilot | nTrust.ai',
  description: 'Turn raw security findings into verified, reversible, multi-format remediation playbooks — without ever exposing infrastructure secrets.',
  metadataBase: new URL('https://trustbrain.ntrust.ai')
}

export const viewport = { width: 'device-width', initialScale: 1 }

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="container">
          <nav className="nav">
            <a href="/" className="brand" style={{ textDecoration: 'none' }}>TrustBrain<span>™</span></a>
            <div className="links">
              <a href="/#why">Why</a>
              <a href="/#positioning">Positioning</a>
              <a href="/portal">Licensing Portal</a>
              <a href="/api/health" target="_blank" rel="noreferrer">API Health</a>
            </div>
          </nav>
        </div>
        {children}
        <div className="container">
          <footer className="footer">
            <div className="row">
              <div>© {new Date().getFullYear()} nTrust.ai — “It&apos;s the numbers we trust.”</div>
              <div>TrustBrain™ · Sovereign AI Security Reasoning Copilot</div>
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
