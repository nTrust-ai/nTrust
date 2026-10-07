import { NextResponse } from 'next/server'
import { TIERS } from '@/lib/tiers'

export const dynamic = 'force-dynamic'

export async function GET() {
  return NextResponse.json({ product: 'TrustBrain™', tiers: TIERS, generatedAt: new Date().toISOString() })
}
