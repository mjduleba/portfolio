// Falls back to localhost for local dev. To override, create an untracked
// frontend/.env.local with NEXT_PUBLIC_API_URL=<your-backend-url>.
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function apiFetch<T>(path: string, options?: RequestInit): Promise<T> {
  const url = new URL(path, API_BASE_URL);

  const response = await fetch(url, {
    ...options,
    // Light ISR-style freshness — this is read-mostly content, not real-time data.
    next: { revalidate: 60 },
  });

  // Throw error for non-200 responses
  if (!response.ok) {
    throw new Error(
      `API request failed: ${response.status} ${response.statusText} for ${url}`
    );
  }

  return response.json() as Promise<T>;
}
