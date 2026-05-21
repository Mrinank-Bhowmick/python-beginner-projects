export default function ScribbleSvg({ color }: { color: string }) {
  return (
    <svg
      style={{
        position: "absolute",
        bottom: -10,
        left: -4,
        right: -4,
        width: "calc(100% + 8px)",
        height: 14,
        overflow: "visible",
      }}
      viewBox="0 0 200 14"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path
        d="M2,8 Q40,1 80,7 T160,6 T198,8"
        stroke={color}
        strokeWidth="4"
        fill="none"
        strokeLinecap="round"
      />
    </svg>
  );
}
