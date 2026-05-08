# Colour palette — rationale + alternatives

Why these specific values, and what to swap if you want a different brand.

## The default palette

| Role | Dark | Light | WCAG AA contrast |
|---|---|---|---|
| Body bg / text | `#0b0d12` / `#e8ecf2` | `#fafbfc` / `#1a1d27` | 14.5 / 14.7 ✓ |
| Muted text | `#8a93a3` on `#0b0d12` | `#58607a` on `#fafbfc` | 5.8 / 6.0 ✓ |
| Accent (orange) | `#d97757` | `#c95a30` | needed darker for white |
| Accent secondary | `#5d8aa8` | `#2f6494` | needed darker for white |
| Accent ok (green) | `#6dba88` | `#3e8e5e` | for lab callouts |

## Why two different accents per mode

`#d97757` (the warm Anthropic-ish orange) reads beautifully on a `#0b0d12`
background — high contrast, low fatigue. But on `#fafbfc`, it's too light:
contrast drops below WCAG AA, and the brand "feels washed out".

`#c95a30` is the same hue family, just deeper. It hits AA on white text
and reads as the same brand orange.

The light variant of `#5d8aa8` (`#2f6494`) and `#6dba88` (`#3e8e5e`) follow
the same darken-for-light-mode rule.

## Common alternative palettes

### Cool / blue brand

```css
:root, [data-theme="dark"] {
  --accent: #5fb4e6;       /* sky blue */
  --accent-glow: rgba(95,180,230,0.35);
}
[data-theme="light"] {
  --accent: #1f7ec0;       /* deeper blue */
  --accent-glow: rgba(31,126,192,0.22);
}
```

### Mono / minimalist

```css
:root, [data-theme="dark"] {
  --accent: #ffffff;       /* monochrome */
  --accent-on: #000000;
}
[data-theme="light"] {
  --accent: #000000;
  --accent-on: #ffffff;
}
```

Note: monochrome puts pressure on hover-states + borders to do the work
that colour normally does. Compensate with thicker borders and stronger shadows.

### Warm / friendly

```css
:root, [data-theme="dark"] {
  --accent: #f4a261;       /* peach */
  --accent-2: #e76f51;     /* coral */
  --accent-3: #2a9d8f;     /* teal */
}
[data-theme="light"] {
  --accent: #d97a3c;
  --accent-2: #c2553a;
  --accent-3: #1f7d72;
}
```

## Don't do

- **Same hex in both modes** — guaranteed contrast failure in one mode.
- **Pure black/pure white surfaces** (`#000` / `#fff`) — too harsh; off-blacks
  (`#0b0d12`) and off-whites (`#fafbfc`) read better and reduce eye strain.
- **More than 2 accent colours** — adds visual noise without semantic gain.
  Use one primary, one secondary, optionally one "ok/error" green/red.
- **Saturated greys** — `#666` reads as muddy. Use cool greys
  (`#8a93a3`) which sit better next to colour accents.

## Verifying contrast

```bash
# Tools to spot-check WCAG ratios:
#   - Chrome DevTools "Inspect" → contrast ratio in colour picker
#   - https://webaim.org/resources/contrastchecker/
```

Aim for:
- **AA Large (≥18px or ≥14px bold):** 3:1 ratio minimum
- **AA Normal (<18px):** 4.5:1 ratio minimum
- **AAA (more accessible):** 7:1 normal / 4.5:1 large

The default palette hits AA across all role-pairs in both modes.
