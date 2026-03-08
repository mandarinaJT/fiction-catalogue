"use client";

import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function HomePage() {
  const [query, setQuery] = useState("");
  const router = useRouter();

  const handleSubmit = (e: React.SubmitEvent) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query)}`);
    }
  };

  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold mb-4">Welcome to Story Catalogue</h1>
      <p className="text-lg text-zinc-400 mb-6">
        All fictional worlds in one place.
      </p>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Browse stories..."
          className="flex-1 px-4 py-2 border rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Search
        </button>
      </form>
      <Link
        href="/login"
        className="px-6 py-2 mt-6 bg-green-600 text-white rounded-lg hover:bg-green-700 inline-block"
      >
        Go to Login
      </Link>
    </main>
  );
}
