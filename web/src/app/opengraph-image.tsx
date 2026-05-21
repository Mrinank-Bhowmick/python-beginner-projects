import { ImageResponse } from "next/og";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const alt = "pyBegin — 250+ Python beginner projects";
export const dynamic = "force-static";

// Static social-share image, generated at build time.
export default function OgImage() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          padding: "80px",
          background: "#fef9ef",
          fontFamily: "sans-serif",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: "20px",
            marginBottom: "28px",
          }}
        >
          <div
            style={{
              width: "84px",
              height: "84px",
              background: "#ff7a59",
              border: "5px solid #1d1830",
              borderRadius: "20px",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: "44px",
            }}
          >
            🐍
          </div>
          <div style={{ fontSize: "44px", fontWeight: 900, color: "#1d1830" }}>
            pyBegin
          </div>
        </div>
        <div
          style={{
            fontSize: "78px",
            fontWeight: 900,
            color: "#1d1830",
            lineHeight: 1.05,
            letterSpacing: "-0.03em",
          }}
        >
          Python that feels good to type.
        </div>
        <div style={{ fontSize: "34px", color: "#5a5470", marginTop: "26px" }}>
          250+ beginner projects · live in-browser playground
        </div>
      </div>
    ),
    { ...size },
  );
}
