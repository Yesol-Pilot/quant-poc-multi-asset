import { createClient } from '@supabase/supabase-js';

/**
 * Server-side Supabase client.
 *
 * Uses the public `anon` key only — every `select` is RLS-gated by the
 * `public_read` policies defined in `supabase/migrations/00001_initial_schema.sql`.
 * Server components are the right place to call this; the client never sees
 * the project URL or anon key beyond what we already render in `<head>` via
 * `NEXT_PUBLIC_*` env vars.
 *
 * No auth, no service role, no writes. This is a read-only surface for the
 * paper-trading dashboard.
 */
const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

export function getSupabaseServerClient() {
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
    // During build without env vars, return a stub that yields empty arrays.
    // Production builds on Vercel always have these set (W1 D2 provisioning).
    return null;
  }
  return createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    auth: { persistSession: false },
  });
}

// Lightweight DB row types — matches supabase/migrations/00001_initial_schema.sql.
// W3+: generate from `supabase gen types typescript` instead of hand-typing.
export type AlphaStatus =
  | 'planned'
  | 'in_progress'
  | 'active'
  | 'paused'
  | 'archived'
  | 'deprecated';

export type AssetClass =
  | 'korean_equity'
  | 'us_equity'
  | 'us_option'
  | 'crypto';

export type AlphaRow = {
  id: string;
  name: string;
  asset_class: AssetClass;
  status: AlphaStatus;
  description: string | null;
  timeframe: string | null;
};

export async function fetchAlphas(): Promise<AlphaRow[]> {
  const supabase = getSupabaseServerClient();
  if (!supabase) return [];

  const { data, error } = await supabase
    .from('alphas')
    .select('id, name, asset_class, status, description, timeframe')
    .order('id', { ascending: true });

  if (error) {
    // Don't crash the page; the dashboard placeholder is still useful.
    console.warn('[supabase] fetchAlphas failed:', error.message);
    return [];
  }
  return (data ?? []) as AlphaRow[];
}
