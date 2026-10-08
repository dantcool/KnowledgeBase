# Donut Math in Python (Pygame)

This project is a Python implementation of the famous ASCII spinning donut, inspired by the original [donut.c](https://www.a1k0n.net/2011/07/20/donut-math.html) by Andy Sloane. The code visualizes a rotating 3D torus (donut) using ASCII characters, rendered in a Pygame window with color cycling.

---

## Background

The original donut code became popular for its clever use of math to render a 3D torus in ASCII art, using only basic trigonometry and a z-buffer for depth. The donut is animated by rotating it in 3D space and projecting the points onto a 2D plane, with luminance (brightness) mapped to different ASCII characters for shading.

For a detailed explanation of the math and rendering technique, see the article: [Donut math: how donut.c works](https://www.a1k0n.net/2011/07/20/donut-math.html).

---

## Mathematical Details

### 1. Torus Parametric Equations
A torus (donut) can be described parametrically using two angles:
- **θ (theta):** Angle around the cross-section of the torus
- **φ (phi):** Angle around the central axis of the torus

Let:
- `R1` = radius of the tube (cross-section)
- `R2` = distance from the center of the tube to the center of the torus

The 3D coordinates of a point on the torus before rotation:

```
(x, y, z) = (R2 + R1 * cosθ, R1 * sinθ, 0)
```

### 2. Rotating the Torus
To animate the donut, we rotate it in 3D space using two angles:
- **A:** Rotation around the X-axis
- **B:** Rotation around the Z-axis

The rotation is performed using rotation matrices. After applying the rotations, the coordinates become:

```
x = circlex * (cosB * cosφ + sinA * sinB * sinφ) - circley * cosA * sinB
y = circlex * (sinB * cosφ - sinA * cosB * sinφ) + circley * cosA * cosB
z = K2 + cosA * circlex * sinφ + circley * sinA
```
Where:
- `circlex = R2 + R1 * cosθ`
- `circley = R1 * sinθ`
- `K2` = distance from viewer to donut (controls perspective)

### 3. 3D to 2D Projection
To display the 3D donut on a 2D screen, we use perspective projection:

```
ooz = 1 / z  # "one over z" (for depth buffering)
xp = screen_width / 2 + K1 * ooz * x
typ = screen_height / 2 - K1 * ooz * y
```
Where:
- `K1` is a scaling factor based on screen size and field of view
- `ooz` is used for z-buffering (depth comparison)

### 4. Surface Normal and Luminance Calculation
To shade the donut, we calculate the surface normal at each point and its dot product with a light direction vector. This gives the luminance (brightness) at that point.

The luminance formula used is:

```
L = cosφ * cosθ * sinB - cosA * cosθ * sinφ - sinA * sinθ + cosB * (cosA * sinθ - cosθ * sinA * sinφ)
```
- If `L > 0`, the surface is facing the viewer and is drawn.
- The value of `L` is mapped to an ASCII character for shading:
  - `.,-~:;=!*#$@` (from dimmest to brightest)

### 5. Z-Buffering
A z-buffer is used to keep track of the closest surface at each screen position. Only points closer to the viewer than previous points are drawn.

---

## How the Code Works

- **3D Torus Rendering:**
  - Loops over `theta` and `phi` to sample points on the torus.
  - Applies 3D rotations and projects each point to 2D.
  - Uses a z-buffer to determine which points are visible.

- **ASCII Shading:**
  - Calculates luminance at each point and selects an ASCII character accordingly.

- **Pygame Display:**
  - Renders the ASCII characters in a Pygame window, with color cycling for visual effect.

---

## Controls
- Press `ESC` or close the window to exit.

---

## Requirements
- Python 3.x
- Pygame

Install dependencies with:
```bash
pip install pygame
```

---

## Running the Program
```bash
python donut.py
```

---

## References
- [Donut math: how donut.c works](https://www.a1k0n.net/2011/07/20/donut-math.html)
- [Original donut.c source code](https://www.a1k0n.net/2011/07/20/donut.c.html)

---

## License
This project is for educational and demonstration purposes, inspired by the public domain original. 