import { NextResponse } from 'next/server'

export const dynamic = 'force-dynamic'

export async function GET() {
  return NextResponse.json({
    status: 'ok',
    product: 'TrustBrain™',
    surface: 'Licensing Portal (Pillar 2/3)',
    version: '0.1.0',
    timestamp: new Date().toISOString()
  })
}
