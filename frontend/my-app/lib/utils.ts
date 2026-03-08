import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export async function fetchWithAuth(url: string) {
  let token = localStorage.getItem("access_token");

  let res = await fetch(url, {
    headers: { Authorization: `Bearer ${token}` },
  });

  if (res.status === 401) {
    // Access token expired → refresh
    const refreshToken = localStorage.getItem("refresh_token");
    const refreshRes = await fetch("http://127.0.0.1:8001/refresh", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh_token: refreshToken }),
    });

    if (refreshRes.ok) {
      const data = await refreshRes.json();
      localStorage.setItem("access_token", data.access_token);

      // Retry original request with new token
      res = await fetch(url, {
        headers: { Authorization: `Bearer ${data.access_token}` },
      });
    } else {
      throw new Error("Refresh failed — user must log in again");
    }
  }

  return res.json();
}
