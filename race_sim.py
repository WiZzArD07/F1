import arcade
import fastf1
import os
import random

# -------------------------------
# Setup Cache
# -------------------------------
os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

print("Loading session...")
session = fastf1.get_session(2024, "Monaco", "R")
session.load()
print("✅ Session loaded!")

# -------------------------------
# Load Drivers
# -------------------------------
drivers = session.drivers[:5]

driver_data = {}

for drv in drivers:
    try:
        laps = session.laps.pick_drivers(drv)
        fastest = laps.pick_fastest()
        tel = fastest.get_telemetry()

        driver_data[drv] = {
            "X": tel['X'].values[::5],
            "Y": tel['Y'].values[::5],
            "color": (
                random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255)
            ),
            "offset": random.randint(0, 200)
        }
    except:
        continue

print("Drivers loaded:", list(driver_data.keys()))

# -------------------------------
# Normalize
# -------------------------------
sample = list(driver_data.values())[0]
X = sample["X"]
Y = sample["Y"]

min_x, max_x = min(X), max(X)
min_y, max_y = min(Y), max(Y)

def normalize(x, y):
    x = (x - min_x) / (max_x - min_x) * 700 + 50
    y = (y - min_y) / (max_y - min_y) * 700 + 50
    return x, y


# -------------------------------
# Window
# -------------------------------
class F1Replay(arcade.Window):
    def __init__(self):
        super().__init__(900, 900, "F1 Replay System 🏎️")
        arcade.set_background_color(arcade.color.BLACK)

        self.frame = 0.0
        self.speed = 1.0
        self.paused = False

    def on_draw(self):
        self.clear()

        # -----------------------
        # Draw Track
        # -----------------------
        for i in range(len(X) - 1):
            dx = abs(X[i+1] - X[i])
            dy = abs(Y[i+1] - Y[i])

            if dx > 1000 or dy > 1000:
                continue

            x1, y1 = normalize(X[i], Y[i])
            x2, y2 = normalize(X[i+1], Y[i+1])
            arcade.draw_line(x1, y1, x2, y2, arcade.color.WHITE, 2)

        # close loop
        x1, y1 = normalize(X[-1], Y[-1])
        x2, y2 = normalize(X[0], Y[0])
        arcade.draw_line(x1, y1, x2, y2, arcade.color.WHITE, 2)

        # -----------------------
        # Draw Cars (SMOOTH)
        # -----------------------
        for drv, data in driver_data.items():
            base = int(self.frame + data["offset"]) % len(data["X"])
            next_idx = (base + 1) % len(data["X"])
            t = self.frame % 1

            x = (1 - t) * data["X"][base] + t * data["X"][next_idx]
            y = (1 - t) * data["Y"][base] + t * data["Y"][next_idx]

            cx, cy = normalize(x, y)
            arcade.draw_circle_filled(cx, cy, 8, data["color"])

        # -----------------------
        # HUD (TOP LEFT)
        # -----------------------
        status = "PAUSED" if self.paused else "PLAYING"
        arcade.draw_text(f"Status: {status}", 20, 860, arcade.color.WHITE, 14)
        arcade.draw_text(f"Speed: {self.speed:.1f}x", 20, 830, arcade.color.WHITE, 14)
        arcade.draw_text(f"Frame: {int(self.frame)}", 20, 800, arcade.color.WHITE, 14)

        arcade.draw_text("Controls:", 20, 750, arcade.color.YELLOW, 14)
        arcade.draw_text("SPACE = Pause/Play", 20, 720, arcade.color.WHITE, 12)
        arcade.draw_text("← → = Step frame", 20, 700, arcade.color.WHITE, 12)
        arcade.draw_text("↑ ↓ = Speed", 20, 680, arcade.color.WHITE, 12)
        arcade.draw_text("R = Restart", 20, 660, arcade.color.WHITE, 12)

    # -----------------------
    # Update Loop
    # -----------------------
    def on_update(self, delta_time):
        if not self.paused:
            self.frame += 0.2 * self.speed

    # -----------------------
    # Controls
    # -----------------------
    def on_key_press(self, key, modifiers):

        # Pause / Play
        if key == arcade.key.SPACE:
            self.paused = not self.paused

        # Restart
        elif key == arcade.key.R:
            self.frame = 0

        # Speed control
        elif key == arcade.key.UP:
            self.speed = min(self.speed + 0.5, 5)

        elif key == arcade.key.DOWN:
            self.speed = max(self.speed - 0.5, 0.1)

        # Frame step (only when paused)
        elif key == arcade.key.RIGHT:
            if self.paused:
                self.frame += 1

        elif key == arcade.key.LEFT:
            if self.paused:
                self.frame -= 1


# -------------------------------
# Run
# -------------------------------
if __name__ == "__main__":
    window = F1Replay()
    arcade.run()