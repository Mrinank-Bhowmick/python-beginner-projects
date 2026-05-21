// Recognition for the contributor who first added a project to the repo.

export default function ProjectCredit({
  author,
  prefix = "Created by",
}: {
  author: string;
  prefix?: string;
}) {
  return (
    <div className="s-credit">
      <span aria-hidden="true">🧑‍💻</span> {prefix}{" "}
      <a
        href={`https://github.com/${author}`}
        target="_blank"
        rel="noreferrer"
      >
        @{author}
      </a>{" "}
      — thank you!
    </div>
  );
}
