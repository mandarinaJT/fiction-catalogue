"use client";

import { fetchWithAuth } from "../../lib/utils";
import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";

export default function SearchPage() {
  const searchParams = useSearchParams();
  const query = searchParams.get("q") || "";
  const [results, setResults] = useState<any[]>([]);

  useEffect(() => {
    if (query) {
      const token = localStorage.getItem("token");
      fetchWithAuth(`http://localhost:8001/search/?q=${query}`).then((data) => {
        if (Array.isArray(data)) {
          setResults(data);
        } else {
          setResults([]);
        }
      });
    }
  }, [query]);

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-6">Results for "{query}"</h1>
      <div className="grid grid-cols-1 md:grid-cols-5 gap-6">
        {results.map((item, idx) => (
          <div key={idx} className="bg-white shadow rounded-lg p-4">
            {/* POSTER IMAGE */}
            <img
              src={item.poster_url}
              alt={item.title}
              style={{
                width: "100%",
                height: "auto",
                objectFit: "contain",
              }}
              className="w-full h-64 object-cover rounded-md mb-4"
            />
            <h2 className="text-xl text-gray-500 font-semibold">
              {item.title}
            </h2>
            <p className="text-gray-500">{item.authors.join(",")}</p>
            <p className="text-sm text-gray-500">Released: {item.year}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
