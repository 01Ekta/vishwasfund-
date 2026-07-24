import { useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export default function App() {
  const [form, setForm] = useState({
    business_type: "",
    location: "",
    monthly_income: "",
  });
  const [matches, setMatches] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/match`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...form,
          monthly_income: Number(form.monthly_income) || 0,
        }),
      });
      const data = await res.json();
      setMatches(data.matches || []);
    } catch (err) {
      console.error("Failed to fetch matches", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <h1 className="text-3xl font-bold mb-2">VishwasFund</h1>
      <p className="text-slate-400 mb-6">
        Find funding, mentors & schemes you can trust.
      </p>

      <form onSubmit={handleSubmit} className="max-w-md space-y-4">
        <input
          name="business_type"
          placeholder="Business type — e.g. tailoring, food stall"
          value={form.business_type}
          onChange={handleChange}
          className="w-full p-3 rounded bg-slate-800 border border-slate-700"
        />
        <input
          name="location"
          placeholder="Location — village / town"
          value={form.location}
          onChange={handleChange}
          className="w-full p-3 rounded bg-slate-800 border border-slate-700"
        />
        <input
          name="monthly_income"
          type="number"
          placeholder="Monthly income (approx.)"
          value={form.monthly_income}
          onChange={handleChange}
          className="w-full p-3 rounded bg-slate-800 border border-slate-700"
        />
        <button
          type="submit"
          disabled={loading}
          className="w-full p-3 rounded bg-amber-400 text-slate-900 font-bold"
        >
          {loading ? "Finding matches..." : "Find My Matches"}
        </button>
      </form>

      {matches && (
        <div className="mt-8 max-w-md space-y-3">
          <h2 className="text-xl font-bold">Your matches</h2>
          {matches.map((m, i) => (
            <div key={i} className="p-4 rounded bg-slate-800 border border-slate-700">
              <div className="font-bold">{m.name}</div>
              <div className="text-slate-400 text-sm">{m.type}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
