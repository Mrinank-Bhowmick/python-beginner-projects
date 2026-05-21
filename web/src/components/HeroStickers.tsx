// Bobbing pile of highlight-project stickers in the hero.

interface StickerItem {
  e: string;
  l: string;
  n: string;
  bg: string;
  pos: React.CSSProperties;
  bob: number;
  rot: number;
}

const ITEMS: StickerItem[] = [
  { e: "🐍", l: "Snake Game", n: "92 lines · pygame", bg: "var(--s-surface-warm)", pos: { top: 6, left: 18 }, bob: 1, rot: -4 },
  { e: "☁️", l: "Weather App", n: "88 lines · requests", bg: "var(--s-surface-cool)", pos: { top: 80, right: 0 }, bob: 2, rot: 3 },
  { e: "🪢", l: "Hangman", n: "78 lines · stdlib", bg: "var(--s-surface-purple)", pos: { top: 215, left: -10 }, bob: 3, rot: 2 },
  { e: "▦", l: "QR Generator", n: "22 lines · qrcode", bg: "var(--s-surface-green)", pos: { top: 290, right: 50 }, bob: 4, rot: -2 },
  { e: "🧮", l: "Calculator", n: "110 lines · tk", bg: "var(--s-surface-yellow)", pos: { top: 400, left: 60 }, bob: 5, rot: 4 },
  { e: "🔐", l: "Password Gen", n: "30 lines · secrets", bg: "#ffd4f0", pos: { top: 410, right: 10 }, bob: 1, rot: -3 },
];

export default function HeroStickers() {
  return (
    <div className="s-stickers" aria-hidden="true">
      {ITEMS.map((s, i) => (
        <div
          key={i}
          className="s-sticker"
          style={{
            ...s.pos,
            background: s.bg,
            animation: `s-bob${s.bob} ${4 + i * 0.3}s ease-in-out infinite`,
            animationDelay: `${-i * 0.7}s`,
            transform: `rotate(${s.rot}deg)`,
          }}
        >
          <span className="emoji">{s.e}</span>
          <div>
            <div className="lbl">{s.l}</div>
            <div className="num">{s.n}</div>
          </div>
        </div>
      ))}
    </div>
  );
}
