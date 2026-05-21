// Small "Runnable" pill — a green dot inside a rounded green chip. Marks
// projects that run live in the in-browser Pyodide playground.

export default function RunnableBadge({
  size = "md",
}: {
  size?: "sm" | "md";
}) {
  return (
    <span
      className={`s-runnable ${size === "sm" ? "sm" : ""}`}
      title="Runs live in the in-browser playground"
    >
      <span className="s-runnable-dot" aria-hidden="true" />
      Runnable
    </span>
  );
}
