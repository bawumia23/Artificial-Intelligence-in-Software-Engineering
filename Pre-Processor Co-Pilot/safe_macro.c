// Safer version – parentheses fix precedence, but side‑effects remain.
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// Even safer for side‑effects: use an inline function (C99+)
static inline int max_safe(int a, int b) { return a > b ? a : b; }
