import { NextResponse } from 'next/server'

export const dynamic = 'force-dynamic'

// Mock license activation — mirrors the Lemon Squeezy webhook flow referenced in ARCH-NT-004 Pillar 2.
// In production this validates a signed webhook and issues/rotates a master license key via the engine.
export async function POST(request) {
  let body = {}
  try { body = await request.json() } catch (_) {}
  const email = (body.email || 'operator@ntrust.ai').toString()
  const tier = (body.tier || 'community').toString()
  const licenseKey = 'TB-' + Math.random().toString(36).slice(2, 8).toUpperCase() + '-' + Math.random().toString(36).slice(2, 6).toUpperCase()
  return NextResponse.json({
    ok: true,
    licenseKey,
    tier,
    email,
    status: 'provisioned',
    note: 'Mock issuance — production activation routes through Lemon Squeezy webhooks + master license key vault.',
    issuedAt: new Date().toISOString()
  })
}
