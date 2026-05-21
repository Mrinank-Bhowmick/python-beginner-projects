// "Paper" — the CodeMirror theme from the Playground design handoff:
// warm parchment editor surface with friendly pastel-on-cream syntax colors.

import { createTheme } from "@uiw/codemirror-themes";
import { tags as t } from "@lezer/highlight";

export const pybeginPaper = createTheme({
  theme: "light",
  settings: {
    background: "#fbf3e0",
    foreground: "#3b3155",
    caret: "#ff7a59",
    selection: "#ffd16645",
    selectionMatch: "#ffd16628",
    lineHighlight: "#00000007",
    gutterBackground: "#f3e8c8",
    gutterForeground: "#bcaa92",
    gutterActiveForeground: "#5a5170",
    fontFamily: "var(--font-mono), 'JetBrains Mono', ui-monospace, monospace",
  },
  styles: [
    { tag: t.comment, color: "#9c8eaf", fontStyle: "italic" },
    {
      tag: [t.keyword, t.operatorKeyword, t.controlKeyword, t.moduleKeyword],
      color: "#c44a8a",
    },
    { tag: [t.string, t.special(t.string)], color: "#a85e1a" },
    { tag: [t.number, t.bool, t.null], color: "#3d6fb5" },
    {
      tag: [t.function(t.variableName), t.function(t.propertyName)],
      color: "#2a8c6e",
    },
    { tag: t.definition(t.variableName), color: "#3b3155" },
    { tag: t.variableName, color: "#3b3155" },
    { tag: [t.className, t.typeName], color: "#c45a2a" },
    { tag: t.propertyName, color: "#2a8c6e" },
    { tag: [t.operator, t.punctuation, t.bracket, t.separator], color: "#5a5170" },
    { tag: [t.self, t.atom], color: "#c45a2a" },
    { tag: t.meta, color: "#9c8eaf" },
  ],
});
